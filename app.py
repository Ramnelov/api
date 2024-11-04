from flask import Flask, request
from waitress import serve

from utils.supabase import supabase

app = Flask(__name__)


@app.route("/")
def index():
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        jwt_token = auth_header.split(" ")[1]
    else:
        return "Missing or invalid JWT token.", 401
    try:
        response = supabase.auth.get_user(jwt_token)
        return f"Hello {response.user.email}!"
    except Exception as e:
        return f"Error: {str(e)}", 400


if __name__ == "__main__":
    # app.run(debug=False)

    serve(app, host="0.0.0.0", port=8080)
