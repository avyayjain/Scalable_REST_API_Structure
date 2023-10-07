import pickle
from API.utils.database.redis_config import redis


def get_user_email_id(uuid):
    user_id = redis.get(uuid)
    user_id = pickle.loads(user_id)
    return user_id["email"]


def save_user_id(email, name, password, uuid):
    user_data_1 = {"email": email,
                   "name": name,
                   "hashed_password": password,
                   "uuid": uuid
                   }
    user_data = pickle.dumps(user_data_1)
    redis.set(uuid, user_data)
    return True


def get_user_name_id(uuid):
    user_id = redis.get(uuid)
    user_id = pickle.loads(user_id)
    return user_id


def get_details(uuid):
    user = redis.get(uuid)
    user = pickle.loads(user)
    user_data_1 = {"email": user["email"],
                   "name": user["name"],
                   "uuid": user["uuid"],
                   }
    return user_data_1


def set_user_name(uuid, name, email, hashed_password):
    user_data_1 = {"email": email,
                   "name": name,
                   "hashed_password": hashed_password,
                   "uuid": uuid
                   }
    user_data = pickle.dumps(user_data_1)
    redis.set(uuid, user_data)
    return user_data_1, uuid
