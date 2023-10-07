from API.utils.common.pwd_helper import get_password_hash
from API.utils.config.constants import DB_CONNECTION_LINK
from API.utils.database.database import Users
from API.utils.database.utils import DBConnection


def create_user(user_email: str, password: str, user_name: str):
    """
    :param user_name:
    :param user_type: type of user admin or user
    :param user_email: User Email
    :param password: User Password
    :return: None
    """
    try:
        with DBConnection(DB_CONNECTION_LINK, False) as db:
            try:
                user = Users(
                    name=user_name,
                    email_id=user_email,
                    hashed_password=get_password_hash(password),
                )
                db.session.add(user)
                db.session.commit()
                return {"message": "user added successfully"}
            except Exception as e:
                print(e)
                raise e
            finally:
                db.session.close()

    except Exception as e:
        print(e)
        raise e


