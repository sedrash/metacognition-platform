def calculate_result(answers):
    if not answers:
        return {
            "score": 0,
            "level": "unknown",
            "strengths": [],
            "weaknesses": ["Aucune réponse fournie"],
            "recommendations": ["Répondre au questionnaire pour obtenir une analyse."]
        }

    category_map = {
        1: "organisation",
        2: "self_assessment",
        3: "adaptation",
        4: "self_knowledge",
        5: "reflection"
    }

    category_scores = {
        "organisation": 0,
        "self_assessment": 0,
        "adaptation": 0,
        "self_knowledge": 0,
        "reflection": 0
    }

    category_counts = {
        "organisation": 0,
        "self_assessment": 0,
        "adaptation": 0,
        "self_knowledge": 0,
        "reflection": 0
    }

    total_score = 0
    max_score = len(answers) * 5

    for item in answers:
        question_id = item.get("question_id")
        value = int(item.get("value", 0))
        total_score += value

        category = category_map.get(question_id)
        if category:
            category_scores[category] += value
            category_counts[category] += 1

    percentage = round((total_score / max_score) * 100, 2) if max_score else 0

    if percentage < 40:
        level = "low"
    elif percentage < 70:
        level = "medium"
    else:
        level = "high"

    strengths = []
    weaknesses = []

    for category, score in category_scores.items():
        count = category_counts[category]
        if count == 0:
            continue
        average = score / count
        if average >= 4:
            strengths.append(category)
        elif average <= 2:
            weaknesses.append(category)

    recommendations = build_recommendations(level, weaknesses)

    return {
        "score": percentage,
        "level": level,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "recommendations": recommendations
    }


def build_recommendations(level, weaknesses):
    recommendations = []

    if level == "low":
        recommendations.append("Commence par planifier des séances de travail courtes et régulières.")
        recommendations.append("Prends quelques minutes après chaque cours pour vérifier ce que tu as compris.")
    elif level == "medium":
        recommendations.append("Tu as déjà de bonnes bases. Essaie d'améliorer la régularité de tes méthodes.")
        recommendations.append("Compare les méthodes qui fonctionnent le mieux pour toi selon la matière.")
    else:
        recommendations.append("Ton niveau de métacognition est bon. Continue à ajuster tes stratégies selon les situations.")
        recommendations.append("Tu peux suivre tes progrès avec un petit bilan après chaque évaluation.")

    weakness_messages = {
        "organisation": "Utilise un planning simple avec des objectifs précis.",
        "self_assessment": "Teste-toi souvent avec des questions ou exercices sans regarder le cours.",
        "adaptation": "Si une méthode ne marche pas, essaie une autre approche comme les fiches ou les exercices.",
        "self_knowledge": "Note les méthodes qui t'aident vraiment à retenir pour mieux te connaître.",
        "reflection": "Après chaque contrôle, analyse ce que tu dois garder et ce que tu dois changer."
    }

    for weakness in weaknesses:
        if weakness in weakness_messages:
            recommendations.append(weakness_messages[weakness])

    return recommendations
