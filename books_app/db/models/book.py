from . import Config
from sqlalchemy.orm import Mapped,mapped_column


Base=Config.BASE

class Book(Base):
    __tablename__="books"


    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    author:Mapped[str]
    release_year:Mapped[int]
    books_quantity:Mapped[int]
