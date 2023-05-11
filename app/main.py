from fastapi import FastAPI, Depends
import schemas, models, database, uvicorn
from sqlalchemy.orm import session
from typing import List
from NLP import work
models.Base.metadata.create_all(database.engine)


app = FastAPI()

@app.post("/Create",  tags=["Text Summarization Module Controller"])
def Summarize_Text(request:schemas.InputText, db:session = Depends(database.get_db)):
    summaraized_txt = work(request.text)
    new_txt = models.user_text(user_name = request.user_name, summarized_text =summaraized_txt)
    db.add(new_txt)
    db.commit()
    db.refresh(new_txt)
    return new_txt

@app.get("/getAll",tags=["Text Summarization Module Controller"])
def Get_All(db:session=Depends(database.get_db)):
    return db.query(models.user_text).all()


    
@app.get("/{id}", response_model=schemas.show, tags=["Text Summarization Module Controller"])
def Search(id:int, db:session=Depends(database.get_db)):
    summaraized_text = db.query(models.user_text).filter(models.user_text.id == id).first()
    return summaraized_text



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
