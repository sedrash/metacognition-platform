from flask import Flask
from app.routes.question_routes import question_bp
from app.routes.response_routes import response_bp
from app.routes.result_routes import result_bp


def create_app():
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False

    @app.get("/")
    def home():
        return {
            "message": "Metacognition API is running",
            "status": "success"
        }

    @app.get("/api/health")
    def health():
        return {
            "status": "ok"
        }

    app.register_blueprint(question_bp, url_prefix="/api/questions")
    app.register_blueprint(response_bp, url_prefix="/api/responses")
    app.register_blueprint(result_bp, url_prefix="/api/results")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
