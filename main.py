import bcrypt
from jose import jwt

database = {}
SECRET_KEY = "super_secret_key_be_careful"

def register_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    database[username] = hashed_password

def login(username, password):
    if username in database:
        hashed_password_from_db = database[username]
        if bcrypt.checkpw(password.encode(), hashed_password_from_db):
            token = jwt.encode({"username": username}, SECRET_KEY, algorithm='HS256')
            return "Bearer " + token
        else:
            return "400 bad request"
    return "400 bad request"

register_user("fernando", "senha123")
token = login("fernando", "senha123")

if token == "400 bad request":
    raise TypeError(token + ": usuario ou senha incorretos!!")

def request(token):
    token_stripped = token.replace("Bearer ", "")
    token_decoded = jwt.decode(token_stripped, SECRET_KEY, algorithms="HS256")
    return token_decoded
    
response = request(token)
print(response)