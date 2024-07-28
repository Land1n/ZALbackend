from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import Boolean
from sqlalchemy import String
from sqlalchemy import Integer


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):

    id: Mapped[int] = mapped_column(Integer,primary_key=True)

    trainings: Mapped[list["Training"]] = relationship(back_populates="training")

    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
