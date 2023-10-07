from fastapi import APIRouter, Depends
from pydantic import BaseModel

from API.resources.token import UserBase, get_current_active_user
from API.utils.functions.redis_func import set_user_name, get_details

test_v1_router = APIRouter()


class SetName(BaseModel):
    name: str


@test_v1_router.post("/setName")
async def set_name(name: SetName, current_user: UserBase = Depends(get_current_active_user)):
    email_id = current_user.email_id
    password = current_user.hashed_password
    uuid = current_user.uuid
    user, uuid = set_user_name(uuid, name.name, email_id, password)

    return {"message": "Name set successfully", "user": user, "uuid": uuid}


@test_v1_router.get("/getName")
async def get_name(current_user: UserBase = Depends(get_current_active_user)):
    try:
        user = get_details(current_user.uuid)
        return {"message": "user details", "user": user}
    except Exception as e:
        return {"message": "User Not Found"}
