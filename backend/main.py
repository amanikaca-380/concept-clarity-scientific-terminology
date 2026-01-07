from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from backend import models, schemas, auth
from backend.database import engine, SessionLocal, Base

from backend.jwt_utils import create_access_token

from fastapi import Request

from backend.jwt_utils import verify_token
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        print("Received signup request:", user)

        hashed_password = auth.hash_password(user.password)

        new_user = models.User(
            username=user.username,
            email=user.email,
            password=hashed_password,
            role=user.role
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {"message": "User created successfully"}

    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token(
        data={"sub": db_user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "username": db_user.username
    }

@app.post("/search")
def save_search(
    data: schemas.SearchTerm,
    request: Request,
    db: Session = Depends(get_db)
):
    auth_header = request.headers.get("Authorization")
    user_email = None

    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        payload = verify_token(token)
        if payload:
            user_email = payload.get("sub")

    # Store only if user is logged in
    if user_email:
        new_search = models.SearchHistory(
            term=data.term,
            user_email=user_email
        )
        db.add(new_search)
        db.commit()

    return {"message": "Search processed successfully"}
