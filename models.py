from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    name = Column(String, index=True)
    department = Column(String)
    doctor = Column(String)
    date = Column(String)
    time = Column(String)
    email = Column(String)
    mobile = Column(String)
