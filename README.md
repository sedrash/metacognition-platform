# 🧠 Metacognition Platform

## 📌 Description

Ce projet est une plateforme web permettant d’évaluer la métacognition d’un utilisateur à travers un questionnaire interactif.

L’objectif est d’aider les utilisateurs à mieux comprendre leur manière d’apprendre et à améliorer leurs méthodes de travail grâce à des recommandations personnalisées.

---

## 🎯 Fonctionnalités

* Questionnaire interactif
* Analyse automatique des réponses
* Calcul d’un score de métacognition
* Identification des points forts et faibles
* Recommandations personnalisées

---

## 🛠️ Technologies utilisées

* **Backend** : Python (Flask)
* **Frontend** : HTML / CSS / JavaScript
* **Base de données** : (à ajouter plus tard)

---

## 📂 Structure du projet

```
metacognition-platform/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── controllers/
│   │   └── services/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── questionnaire.html
│   ├── result.html
│   └── style.css
│
└── README.md
```

---

## 🚀 Installation et lancement

### 1. Cloner le projet

```
git clone https://github.com/TON-USERNAME/metacognition-platform.git
cd metacognition-platform
```

---

### 2. Lancer le backend

```
cd backend
python -m venv venv
```

#### Windows

```
venv\Scripts\activate
```

#### Linux / macOS

```
source venv/bin/activate
```

```
pip install -r requirements.txt
python main.py
```

---

## 🌐 API disponible

* `GET /` → vérifier que le serveur fonctionne
* `GET /api/health` → état du serveur
* `GET /api/questions/` → récupérer les questions
* `POST /api/responses/` → envoyer les réponses
* `GET /api/results/<id>` → récupérer les résultats

---

## 📥 Exemple de requête

```
POST /api/responses/
```

```json
{
  "answers": [
    {"question_id": 1, "value": 4},
    {"question_id": 2, "value": 3},
    {"question_id": 3, "value": 5},
    {"question_id": 4, "value": 2},
    {"question_id": 5, "value": 4}
  ]
}
```

---

## 👥 Équipe

* Front-end : Interface utilisateur
* Back-end : API Flask
* Base de données : Gestion des données
* Analyse : Scoring et recommandations

---

## ✅ Objectif pédagogique

Ce projet permet de mettre en pratique :

* le développement web
* les API REST
* la gestion des données
* le travail en équipe

---

## 📌 Améliorations possibles

* Ajouter une base de données (SQLite / PostgreSQL)
* Ajouter une authentification utilisateur
* Améliorer l’analyse avec de l’intelligence artificielle
* Ajouter un tableau de bord utilisateur

---

## 📄 Licence

Projet réalisé dans un cadre pédagogique.
