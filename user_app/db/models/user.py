from sqlalchemy.orm import Mapped,mapped_column
from . import Config

Base = Config.BASE

class User(Base):
    __tablename__="users"


    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    surname:Mapped[str]
    email:Mapped[str]
    password:Mapped[str]
    phone_number:Mapped[int]
    