from importlib.metadata import metadata
import databases
import sqlalchemy

import ormar


engine = sqlalchemy.create_engine("postgresql://krzyzak:test@postgres:5432/test")
database = databases.Database("postgres://krzyzak:test@postgres:5432/test")
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
