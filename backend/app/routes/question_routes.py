from flask import Blueprint

question_bp = Blueprint("questions", __name__)

QUESTIONS = [
    {
        "id": 1,
        "text": "Avant de commencer à réviser, est-ce que tu organises ton travail ?",
        "type": "scale",
        "category": "organisation",
        "options": [1, 2, 3, 4, 5]
    },
    {
        "id": 2,
        "text": "Est-ce que tu vérifies si tu as compris après une leçon ?",
        "type": "scale",
        "category": "self_assessment",
        "options": [1, 2, 3, 4, 5]
    },
    {
        "id": 3,
        "text": "Quand une méthode ne marche pas, est-ce que tu en changes ?",
        "type": "scale",
        "category": "adaptation",
        "options": [1, 2, 3, 4, 5]
    },
    {
        "id": 4,
        "text": "Est-ce que tu sais quelles méthodes t'aident le plus à apprendre ?",
        "type": "scale",
        "category": "self_knowledge",
        "options": [1, 2, 3, 4, 5]
    },
    {
        "id": 5,
        "text": "Après un contrôle, est-ce que tu réfléchis à ce qui a marché ou non ?",
        "type": "scale",
        "category": "reflection",
        "options": [1, 2, 3, 4, 5]
    }
]


@question_bp.get("/")
def get_questions():
    return {
        "status": "success",
        "count": len(QUESTIONS),
        "data": QUESTIONS
    }
