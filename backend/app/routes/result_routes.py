from flask import Blueprint
from app.controllers.response_controller import get_result

result_bp = Blueprint("results", __name__)


@result_bp.get("/<int:submission_id>")
def fetch_result(submission_id):
    record = get_result(submission_id)

    if not record:
        return {
            "status": "error",
            "message": "Result not found."
        }, 404

    return {
        "status": "success",
        "data": record
    }
