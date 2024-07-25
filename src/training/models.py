from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

training = Table(
    "training",
    metadata,
    Column()
)