from flask import Flask, redirect, request, session, url_for
from google_auth_oauthlib.flow import Flow
import os

app = Flask(__name__)
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://aura-mail-7ff59cff.base44.app"])


app.secret_key = os.environ.get("SECRET_KEY")

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # for local testing

CLIENT_ID = os.environ.get("882453387713-okjvaacihogq8s3fdq0rqu19r0vu7lui.apps.googleusercontent.com")
CLIENT_SECRET = os.environ.get("****Fwmc")
REDIRECT_URI = os.environ.get("http://localhost:5000/oauth2callback")

@app.route('/')

def home():
    return 'Welcome to SmartMail Backend!'

@app.route('/auth')
def auth():
    flow = Flow.from_client_config({
        "web": {
            "client_id": 882453387713-okjvaacihogq8s3fdq0rqu19r0vu7lui.apps.googleusercontent.com,
            "client_secret": "****Fwmc",
            "redirect_uris": ["http://localhost:5000/oauth2callback"],
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token"
        }
    }, scopes=['https://www.googleapis.com/auth/gmail.readonly'])

    flow.redirect_uri = REDIRECT_URI
    authorization_url, _ = flow.authorization_url(prompt='consent')
    return redirect(authorization_url)

@app.route('/oauth2callback')
def oauth2callback():
    return "Gmail Authentication Successful! ✅"

if __name__ == '__main__':
    app.run(debug=True)
