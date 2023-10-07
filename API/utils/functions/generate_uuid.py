import uuid


def generate_uuid():
    auth_token = str(uuid.uuid4())

    return auth_token
