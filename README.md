# holbertonschool-higher_level_programming
```mermaid
classDiagram
direction TB

class BaseModel{
-id : str
+created at : time
+updated at : time
}
class User{
+First name
-Last name
-Email
-user.id
#Password
~def create_user()
#def change_permission()
~def del_user()
~def modify_user()
+def list_user_place()
}
class Place{
+Title
+Description
+Price
+Latitude
+Longitude
+Owner = user.id
~def create_place()
~def modify_place()
~def del_place()
}
class Amenity{
+Name
+Description
~def create_amenity()
~def modify_amenity()
~def del_amenity()
}
class Review{
+Place
+User
+Rating
+Comment
-user.id
~def create_review()
~def modify_review()
~def del_review()
}

BaseModel --|> User : Inheritance
BaseModel --|> Place : Inheritance
BaseModel --|> Amenity : Inheritance
BaseModel --|> Review : Inheritance
linkStyle 0,1,2,3 stroke:#800080,stroke-width:3px;

Place <.. Amenity : Dependency
linkStyle 4 stroke:#FFA500,stroke-width:3px;

Place <--> Review : Association
User <--> Review : Association
User <--> Place : Association
linkStyle 5,6,7 stroke:#0000FF,stroke-width:3px;

style BaseModel fill:#d3d3d3,stroke:#000,stroke-width:2px;
style User fill:#ADD8E6,stroke:#000,stroke-width:2px;
style Place fill:#90EE90,stroke:#000,stroke-width:2px;
style Amenity fill:#FFA500,stroke:#000,stroke-width:2px;
style Review fill:#FF6347,stroke:#000,stroke-width:2px;
```
