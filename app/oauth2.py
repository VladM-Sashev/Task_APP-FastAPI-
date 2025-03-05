from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . config import settings

token_bearer = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY=settings.secret_key
ALGORITHM=settings.algorithm
TIME_ACCESS_TOKEN=settings.time_access_token

def create_access_token(payload: dict):
    to_encode = payload.copy()
    expire = datetime.now() + timedelta(minutes=TIME_ACCESS_TOKEN)
    to_encode.update({"exp": expire})
    jwt_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token

def verify_access_token(token: str, credential_exceptions):
    try:

        token_decode = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: int =token_decode.get("user_id")
        if not id:
          raise credential_exceptions
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credential_exceptions
    return token_data


def get_current_user(token: str = Depends(token_bearer)):
    credential_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not verify credentials!", 
    headers={"WWW-Authenticate": "Bearer"})
    return verify_access_token(token, credential_exception)