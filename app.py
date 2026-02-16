from flask import Flask
from extensions import mongo, jwt
from config import Config
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    jwt.init_app(app)

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    from routes.auth import auth_bp
    from routes.video import video_bp
    from routes.progress import progress_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(video_bp, url_prefix="/video")
    app.register_blueprint(progress_bp, url_prefix="/progress")

    @app.route("/health")
    def health():
        return {"status": "ok"}


    

    @app.route("/pingdb")
    def pingdb():
      try:
        mongo.db.users.find_one()
        return {"status": "MongoDB connected"}
      except Exception as e:
        return {"error": str(e)}

   

    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
