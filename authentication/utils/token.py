from jwt import decode
from decouple import config


class JWTToken:
    def get_payload(token: str):
        return decode(token, config("JWT_SECRET_KEY"), ["HS256"])
