from . import Config
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey


Base=Config.BASE


class User(Base):
    __tablename__="users"

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    event_id:Mapped[int] = mapped_column(ForeignKey("events.id"))
    event:Mapped["Event"] = relationship(back_populates="user")