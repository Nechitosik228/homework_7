from ..schemas import CreateUser
from . import app
from db import User,Config

Session=Config.SESSION

@app.post("/registration")
def register(data:CreateUser):
    with Session.begin() as session:
        user = User(**data.model_dump())
        session.add(user)
        return user