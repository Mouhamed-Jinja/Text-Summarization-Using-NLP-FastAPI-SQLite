from database import Base
from sqlalchemy import Column , Integer, String
class user_text(Base):
    __tablename__ = "summaraized"
    id = Column(Integer, primary_key=True , index=True)
    user_name = Column(String)
    summarized_text = Column(String)
   