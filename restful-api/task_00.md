# 📡 Basics of HTTP/HTTPS

## 📌 Background
Le **Hypertext Transfer Protocol (HTTP)** est le protocole fondamental de communication sur le Web. Il permet aux clients (comme les navigateurs) d’interagir avec les serveurs web pour récupérer et envoyer des données.

Avec l’évolution du web et la nécessité de protéger les échanges, une version sécurisée appelée **HTTPS (HTTP Secure)** a été introduite. HTTPS ajoute une couche de chiffrement via **SSL/TLS**, protégeant ainsi les données contre l’interception et la falsification.

---

## 🎯 Objectifs
- Différencier **HTTP et HTTPS**.
- Comprendre la **structure** des requêtes et réponses HTTP.
- Reconnaître et expliquer les **méthodes HTTP** et les **codes de statut HTTP**.

---

## 📚 Ressources
- [📖 MDN - Introduction à HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [🔐 Différences entre HTTP et HTTPS](https://developer.mozilla.org/en-US/docs/Web/HTTP/HTTP_vs_HTTPS)
- [📜 Liste des codes de statut HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

## 🛡️ 1. Différences entre HTTP et HTTPS
| Critère      | HTTP  | HTTPS  |
|-------------|------|--------|
| **Sécurité** | Pas sécurisé, les données circulent en clair | Chiffré avec **SSL/TLS**, protégé contre l’interception |
| **Port** | 80 | 443 |
| **Certificat** | Pas nécessaire | Utilise un **certificat SSL** |
| **Utilisation** | Sites sans données sensibles | Sites avec transactions, authentifications, données personnelles |

💡 **Pourquoi utiliser HTTPS ?**
- **Empêche le vol de données** (ex: mots de passe, cartes bancaires).
- **Vérifie l’identité du serveur** via un **certificat SSL**.
- **Améliore le SEO** (Google favorise les sites HTTPS dans les résultats de recherche).

---

## 🔍 2. Structure d'une Requête et Réponse HTTP
Vous pouvez explorer cela en utilisant les **outils de développement** d’un navigateur :

1. **Clic droit** sur une page web → **Inspecter**.
2. Aller dans l’onglet **Network** (Réseau).
3. Recharger la page et examiner la première requête.

### 📤 Structure d’une requête HTTP
- **GET** : Méthode HTTP.
- **/index.html** : Ressource demandée.
- **HTTP/1.1** : Version du protocole.
- **Host** : Serveur ciblé.
- **User-Agent** : Informations sur le navigateur.

### 📥 Structure d’une réponse HTTP
- **200 OK** : Code de statut.
- **Date** : Heure de la réponse.
- **Server** : Logiciel du serveur.
- **Content-Type** : Type de contenu renvoyé.

---

## 🔄 3. Méthodes HTTP et Codes de Statut

### 📌 Méthodes HTTP
| Méthode  | Description | Exemple d'utilisation |
|----------|------------|----------------------|
| **GET**  | Récupère une ressource | Charger une page web |
| **POST** | Envoie des données | Soumettre un formulaire |
| **PUT**  | Modifie une ressource | Modifier un profil utilisateur |
| **DELETE** | Supprime une ressource | Supprimer un commentaire |

### 📌 Codes de Statut HTTP
| Code | Signification | Exemple |
|------|-------------|--------|
| **200 OK** | Succès | Page chargée sans problème |
| **301 Moved Permanently** | Redirection | Site déplacé vers une nouvelle URL |
| **403 Forbidden** | Accès refusé | Page nécessitant une authentification |
| **404 Not Found** | Ressource introuvable | Page supprimée ou URL erronée |
| **500 Internal Server Error** | Erreur serveur | Bug ou surcharge du serveur |

---

## 🛠️ Exercices Pratiques
### 1️⃣ Observer une requête HTTP
📌 **Objectif** : Examiner les requêtes HTTP en inspectant un site web.

**Étapes :**
1. Ouvrez [https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts).
2. Ouvrez les **Outils de développement** (`F12` ou `Ctrl + Shift + I`).
3. Allez dans **Network**, rechargez la page et cliquez sur la requête principale.
4. Observez la requête et la réponse.

---

### 2️⃣ Tester les requêtes avec `curl`
📌 **Objectif** : Utiliser `curl` pour interagir avec une API REST.

**1. Obtenir des données d’une API**
```sh
curl https://jsonplaceholder.typicode.com/posts
