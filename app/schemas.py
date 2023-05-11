from pydantic import BaseModel
from typing import Optional, List
class InputText(BaseModel):
    text :str
    user_name :Optional[str] = None
    
class show(BaseModel):
    summarized_text :Optional[str] = None
    user_name :Optional[str] = None
    class Config():
        orm_mode= True
    

    