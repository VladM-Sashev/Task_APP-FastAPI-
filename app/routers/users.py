from fastapi import FastAPI,Depends, APIRouter
from sqlalchemy.orm import Session
from fastapi import HTTPException,status,Response
from ..database  import get_db
from .. import models, schemas, utils, oauth2


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# get users
@router.get("/",status_code=status.HTTP_201_CREATED,response_model=list[schemas.UserInfo])
def get_users(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    all_users = db.query(models.User).all()
    return all_users
# create user path operation
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserInfo)
def create_user(user: schemas.PostUser, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# get user by id path operatiuon
@router.get("/{id}",status_code=status.HTTP_201_CREATED,response_model=schemas.UserInfo)
def get_UserID(id: int, db: Session =Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    single_user = db.query(models.User).filter(models.User.id==id).first()
    if not single_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id}, does not exist!")
    return single_user

# delete user path operation
@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    deleted_user = db.query(models.User).filter(models.User.id==id)
    if not deleted_user.delete():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id: {id}, does not exist!")
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
