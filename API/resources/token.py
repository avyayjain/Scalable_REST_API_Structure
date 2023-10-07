import pickle
from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel, EmailStr

from API.utils.common.pwd_helper import verify_password
from API.utils.config.constants import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from API.utils.database.redis_config import redis
from API.utils.functions.find_user import find_user_pass_email, find_user_pass_email_id
from API.utils.functions.generate_uuid import generate_uuid
from API.utils.functions.redis_func import save_user_id, get_user_email_id

token_router = APIRouter()


# Need to Check how Imenso is doing their validation
#
# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
#
#
# def check_email(email):
#     if (re.search(regex, email)):
#         return email
#     else:
#         raise


class AuthUser(BaseModel):
    email_id: EmailStr
    password: str


class LogoutUser(BaseModel):
    email_id: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    uuid: Optional[str] = None


class UserBase(BaseModel):
    email_id: EmailStr
    name: str
    hashed_password: str
    uuid: Optional[str] = None


class UserInDB(UserBase):
    hashed_password: str


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_details(uuid):
    user = redis.get(uuid)
    user = pickle.loads(user)
    return UserInDB(
        uuid=user["uuid"],
        email_id=user["email"],
        hashed_password=user["hashed_password"],
        name=user["name"], )


def authenticate_user(email_id: str, password: str):
    """

    :param email_id: Resource ID
    @type email_id: str
    :param password: User Password
    @type password: str
    @return: User Object
    @rtype: object
    """
    try:
        hash_pass, name = find_user_pass_email_id(email_id)

    except Exception as e:
        return False
    if not verify_password(password, hash_pass):
        return False
    return UserInDB(
        email_id=email_id,
        hashed_password=hash_pass,
        name=name

    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """

    @param token: token is used to check credentials
    @type token: str
    @return: user object
    @rtype: object
    """

    try:
        uuid: str = token
        token_data = TokenData(uuid=uuid)

    except Exception as e:
        return e

    try:
        user = get_details(uuid=token_data.uuid)
    except Exception as e:
        raise e

    if user is None:
        return {"message": "User Not Found"}
    return user


async def get_current_active_user(current_user: UserBase = Depends(get_current_user)):
    """

    @param current_user: User Object
    @type current_user: Object
    @return: User Object
    @rtype: Object
    """
    try:
        return current_user
    except Exception as e:
        print(e)
        raise e


@token_router.post("", response_model=Token)
async def login_for_access_token(form_data: AuthUser):
    """
    API For Token Authorisation username

    """

    try:
        user = authenticate_user(form_data.email_id, form_data.password)

    except Exception as e:
        raise e
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            headers={"WWW-Authenticate": "Bearer"},
        )
    uuid = generate_uuid()
    email = user.email_id
    name = user.name
    password = user.hashed_password

    try:
        save_user_id(email, name, password, uuid=uuid)
    except Exception as e:
        raise e
    return {"access_token": uuid, "token_type": "bearer"}
