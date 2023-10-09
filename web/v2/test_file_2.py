import pickle

from fastapi import APIRouter, Depends

from API.resources.token import UserBase, get_current_active_user
from API.utils.database.redis_config import redis

test_v2_router = APIRouter()


@test_v2_router.get("/get_all_data")
async def get_all_data(current_user: UserBase = Depends(get_current_active_user)):
    user_data = {}
    keys = redis.keys('*')
    for key in keys:
        value = redis.get(key)
        if value is not None:
            # Deserialize the stored dictionary
            try:
                data_dict = pickle.loads(value)
                user_data[key] = data_dict
            except (pickle.UnpicklingError, TypeError) as e:
                print(f"Failed to unpickle data for key '{key}': {e}")
    return {"message": "the data in redis is", "data": user_data}
