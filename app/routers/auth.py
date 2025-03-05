from fastapi import HTTPException, status, APIRouter, Depends
from .. import schemas, database, models, utils, oauth2
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/login',
    tags=['Authentication']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def login(user_details:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email==user_details.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid credentials!")
    if not utils.verify(user_details.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid credentials!")
    access_token = oauth2.create_access_token(payload={"user_id": user.id})
    return {"access_token": access_token,"token_type": "Bearer"}