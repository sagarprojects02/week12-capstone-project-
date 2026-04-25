from jose import jwt

SECRET = "secret"

def login_user(data):
    if data["email"] == "user@gmail.com":
        token = jwt.encode({"user": data["email"]}, SECRET, algorithm="HS256")
        return {"token": token}
    return {"error": "Invalid"}
