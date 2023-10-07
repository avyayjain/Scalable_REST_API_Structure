from sqlalchemy import (
    ARRAY,
    JSON,
    TEXT,
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String, Sequence,
)

from sqlalchemy.ext.declarative import declarative_base

from API.utils.database.utils import CustomBaseModel

Base = declarative_base(cls=CustomBaseModel)


class Users(Base):
    __tablename__ = "user_info"
    email_id = Column(String, primary_key=True, unique=True, nullable=False)
    name = Column(
        String,
        unique=True,
    )

    hashed_password = Column(String, nullable=False)
