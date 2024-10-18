from . import Config
from sqlalchemy.orm import Mapped,mapped_column,relationship
from datetime import datetime
from typing import List


Base=Config.BASE


class Event(Base):
    __tablename__="events"

    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str]
    date:Mapped[datetime]
    user: Mapped[List["User"]] = relationship(back_populates="event")
    