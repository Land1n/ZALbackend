from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass

association_table_training_exercise = Table(
    "association_table",
    Base.metadata,
    Column("exercise_id", ForeignKey("exercise.id"), primary_key=True),
    Column("training_id", ForeignKey("training.id"), primary_key=True),
)

class Exercise(Base):
    __tablename__ = 'exercise'

    id: Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(50),nullable=False)
    weight :Mapped[int] = mapped_column(Integer,nullable=False)
    repetitions :Mapped[int] = mapped_column(Integer,nullable=False)
    round :Mapped[int] = mapped_column(Integer,nullable=False)
    annotation:Mapped[str] = mapped_column(String(150),nullable=True)
    training: Mapped[list["Training"]] = relationship(
        secondary=association_table_training_exercise,
        back_populates="training"
    )

class Training(Base):
    __tablename__ = "training"

    id: Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(String(50),nullable=False)
    subtitle:Mapped[str] = mapped_column(String(100),nullable=False)
    annotation:Mapped[str] = mapped_column(String(150),nullable=True)
    children: Mapped[list["Exercise"]] = relationship(
        secondary=association_table_training_exercise,
        back_populates="exercise"
    )
