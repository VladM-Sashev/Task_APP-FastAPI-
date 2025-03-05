from fastapi import FastAPI,Depends, APIRouter
from sqlalchemy.orm import Session
from fastapi import HTTPException,status,Response
from ..database import get_db
from typing import Optional
from .. import models, schemas, oauth2



router = APIRouter(
   prefix="/tasks",
   tags=["Tasks"]
)
# get path operation route
@router.get("/",status_code=status.HTTP_201_CREATED, response_model=list[schemas.TaskResponse])
async def get_tasks(db:Session = Depends(get_db) , current_user: int = Depends(oauth2.get_current_user),
                    limit: int = 10, skip: int = 0):
     all_tasks =db.query(models.Task).filter(models.Task.owner_id==current_user.id).limit(limit).offset(skip).all()
     return  all_tasks

# get by id
@router.get("/{id}",status_code=status.HTTP_201_CREATED,response_model=schemas.TaskResponse)
async def get_taskId(id: int,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    single_task = db.query(models.Task).filter(models.Task.id==id).first()
    if not single_task:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Task with id: {id}, does not exist")
    if single_task.owner_id != current_user.id:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Unauthorized action")
    return single_task
# post path operation route
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.TaskResponse)
async def create_task(task: schemas.PostTask, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_task = models.Task(owner_id=current_user.id,**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
# update path operation route
@router.put("/{id}",status_code=status.HTTP_201_CREATED,response_model=schemas.UpdateTask)
async def update_task(id:int,task:schemas.PostTask,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    update_query = db.query(models.Task).filter(models.Task.id==id)
    updated_task = update_query.first()
    if not updated_task:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Task with id: {id}, does not exist!")
    if updated_task.owner_id != current_user.id:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized action!")
    update_query.update(task.dict())
    db.commit()
    db.refresh(updated_task)
    
    return update_query.first()
# delete path operation route
@router.delete("/{id}")
async def delete_task(id: int,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
 delete_query=db.query(models.Task).filter(models.Task.id==id).first()
 if not delete_query:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id: {id}, does not exist!")
 if delete_query.owner_id != current_user.id:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Unauthorised action.")
 db.delete(delete_query)
 db.commit()
 return Response(status_code=status.HTTP_204_NO_CONTENT)