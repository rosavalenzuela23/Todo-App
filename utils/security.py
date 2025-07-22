from csv import Error
from dotenv import load_dotenv
import jwt
import os
from passlib.context import CryptContext

load_dotenv()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

PRIVATE_KEY = os.getenv("PRIV_KEY")
PUBLIC_KEY = os.getenv("PUB_KEY")
if not PRIVATE_KEY or not PUBLIC_KEY:
    raise Error("There's no private or public key to sign/verify tokens")

def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)

def get_password_hash(plain_password: str):
    return pwd_context.hash(plain_password)

def create_access_token(data: dict, expires_delta: int) -> str:
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, str(PRIVATE_KEY), "RS256")

    return encoded_jwt

def decode_jwt(token: str) -> str:
    decoded_token = jwt.decode(token, str(PUBLIC_KEY), "RS256")
    return decoded_token
