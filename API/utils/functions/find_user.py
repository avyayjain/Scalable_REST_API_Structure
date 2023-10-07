from API.utils.config.constants import DB_CONNECTION_LINK
from API.utils.database.database import Users
from API.utils.database.utils import DBConnection


def find_user_pass_email(email_id):
    """

    @param user_email: User Email
    @type user_email: str
    @return: hashed password and data disable
    @rtype: Tuple[str,bool]
    """
    try:
        with DBConnection(DB_CONNECTION_LINK, False) as db:
            try:
                data = (
                    db.session.query(Users).filter(Users.email_id == email_id).first()
                )
                if not data:
                    return {"message": "user not found"}
                if data.hashed_password:
                    hash_pass = data.hashed_password
                    return hash_pass, email_id
                else:
                    raise Exception
            except Exception as e:
                raise e

            finally:
                db.session.close()
    except Exception as e:
        raise


def find_user_pass_email_id(email_id):

    try:
        with DBConnection(DB_CONNECTION_LINK, False) as db:
            try:
                data = (
                    db.session.query(Users).filter(Users.email_id == email_id).first()
                )
                if not data:
                    return {"message": "user not found"}
                if data.hashed_password:
                    hash_pass = data.hashed_password
                    name = data.name
                    return hash_pass, name
                else:
                    raise Exception
            except Exception as e:
                raise e

            finally:
                db.session.close()

    except Exception as e:
        raise e
