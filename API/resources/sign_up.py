from fastapi import APIRouter
from pydantic import BaseModel

from API.utils.functions.add_user import create_user

add_user_router = APIRouter()


class AuthAddUser(BaseModel):
    email: str
    password: str
    name: str


class DeleteUser(BaseModel):
    email: str


@add_user_router.post("/")
async def sign_up(
        form_data: AuthAddUser
):
    """
    API to ADD Users

    """
    try:
        create_user(
            user_email=form_data.email,
            password=form_data.password,
            user_name=form_data.name,
        )
        return {"detail": "User Added ,please login to continue"}
    except Exception as e:
        print(e, "error")
