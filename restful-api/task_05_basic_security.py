from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)

app = Flask(__name__)


app.config['JWT_SECRET_KEY'] = 'uniq_key'
jwt = JWTManager(app)


auth = HTTPBasicAuth()


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    verify password and auth
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    If Success return "Basic Auth: Access Granted".
    """
    return jsonify({"message": "Basic Auth: Access Granted"}), 200


@app.route('/login', methods=['POST'])
def login():
    """
    login root
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"message": "user or password invalid"}), 401

    additional_claims = {"role": user["role"]}
    access_token = create_access_token(
        identity=username, additional_claims=additional_claims)
    return jsonify({"access_token": access_token}), 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    Token valid, return "JWT Auth: Access Granted".
    """
    return jsonify({"message": "JWT Auth: Access Granted"}), 200


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    Verify and return "Admin Access: Granted" if admin,
    or error 403.
    """
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200


@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({"msg": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token_response(callback):
    return jsonify({"msg": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token_response(jwt_header, jwt_payload):
    return jsonify({"msg": "Token expired"}), 401


if __name__ == '__main__':
    app.run(debug=True)
