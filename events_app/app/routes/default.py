from db import Config,Event,User
from ..schemas import CreateEvent,EditEvent,RescheduleEvent,RegisterForEvent
from . import app
from sqlalchemy import select,update
from fastapi import HTTPException


Session=Config.SESSION

@app.post("/events",status_code=201)
def create_event(data:CreateEvent):
    with Session.begin() as session:
        event = Event(**data.model_dump())
        session.add(event)
        return event
    
@app.get("/events")
def all_events():
    with Session() as session:
        events=session.scalars(select(Event)).all()
        if events:
            return events
        else:
            raise HTTPException(status_code=204,detail="No content")
@app.get("/events/{id}")
def one_event(id:int):
    with Session() as session:
        event = session.scalar(select(Event).where(Event.id==id))
        if event:
            return event
        else: 
            raise HTTPException(status_code=404,detail="Not found")        

@app.put("/events/{id}")
def edit_event(id:int,data:EditEvent):
    with Session.begin() as session:
        event = session.scalar(select(Event).where(Event.id==id))
        if event:
            edit=update(Event).where(Event.id==id).values(title=data.title,date=data.date)
            session.execute(edit)
            return event
        else:
            raise HTTPException(status_code=404,detail="Not found")
        

@app.delete("/events/{id}")
def del_event(id:int):
    with Session.begin() as session:
        event = session.scalar(select(Event).where(Event.id==id))
        if event:
            session.delete(event)
            return event
        else:
            raise HTTPException(status_code=404,detail="Not found")
        

@app.patch("/events/{id}/reschedule")
def reschedule_event(id:int,data:RescheduleEvent):
    with Session.begin() as session:
        event = session.scalar(select(Event).where(Event.id==id))
        if event:
            edit=update(Event).where(Event.id==id).values(title=event.title,date=data.date)
            session.execute(edit)
            return event
        else:
            raise HTTPException(status_code=404,detail="Not found")
        


@app.post("/events/{id}/rspv")
def register(data:RegisterForEvent,id:int):
    with Session.begin() as session:
        user=session.scalar(select(User).where(User.name==data.name))
        if user:
            event=session.scalar(select(Event).where(Event.id==id))
            if event:
                user_check=session.scalar(select(User).where(User.name==data.name).where(User.event_id==id))
                if user_check:
                    raise HTTPException(status_code=409,detail="You are already registered for this event")
                edit=update(User).where(User.name==data.name).values(name=data.name,event_id=id)
                session.execute(edit)
                return "You are registered"
            else:
                raise HTTPException(status_code=404,detail="No event with this id")
        else:
            event=session.scalar(select(Event).where(Event.id==id))
            if event:
                add_user=User(name=data.name,event_id=id)
                session.add(add_user)
                return "You are registered"
            else:
                raise HTTPException(status_code=404,detail="No event with this id")