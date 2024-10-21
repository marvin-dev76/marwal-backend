from flask import Flask
from routes.router import router

app = Flask(__name__)

app.register_blueprint(router)

app.config["UPLOAD_FOLDER"] = "uploads"

if __name__ == "__main__":
    app.run(debug=True, port=3000)
