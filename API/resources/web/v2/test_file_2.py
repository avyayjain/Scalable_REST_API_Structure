from fastapi import APIRouter, Depends

from API.resources.token import UserBase, get_current_active_user

test_v2_router = APIRouter()


@test_v2_router.get("/hello")
async def hello(current_user: UserBase = Depends(get_current_active_user)):
    return {"message": "Hello World"}
