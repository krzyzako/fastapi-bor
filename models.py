from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine


class Movies(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    genre: str
    sensitive: Optional[bool] = False


movie_1 = Movies(name="Fight Club", genre="Thriller",sensitive=True)

engine = create_engine("postgresql://krzyzak:test@postgres:5432/test")


SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(movie_1)
    session.commit()