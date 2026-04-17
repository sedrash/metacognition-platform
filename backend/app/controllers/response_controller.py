from app.services.scoring_service import calculate_result

# Temporary in-memory storage for demo purposes
SUBMISSIONS = {}
CURRENT_ID = 1


def save_responses(payload):
    global CURRENT_ID

    answers = payload.get("answers", [])
    result = calculate_result(answers)

    submission_id = CURRENT_ID
    SUBMISSIONS[submission_id] = {
        "id": submission_id,
        "answers": answers,
        "result": result
    }
    CURRENT_ID += 1

    return SUBMISSIONS[submission_id]


def get_result(submission_id):
    return SUBMISSIONS.get(submission_id)
