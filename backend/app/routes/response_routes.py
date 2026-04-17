from flask import Blueprint, request
from app.controllers.response_controller import save_responses

response_bp = Blueprint("responses", __name__)


@response_bp.post("/")
def submit_responses():
    payload = request.get_json(silent=True)

    if not payload or "answers" not in payload:
        return {
            "status": "error",
            "message": "Invalid payload. Expected JSON with an 'answers' field."
        }, 400

    answers = payload.get("answers", [])
    if not isinstance(answers, list) or len(answers) == 0:
        return {
            "status": "error",
            "message": "Answers must be a non-empty list."
        }, 400

    record = save_responses(payload)

    return {
        "status": "success",
        "message": "Responses submitted successfully.",
        "submission_id": record["id"],
        "result": record["result"]
    }, 201
