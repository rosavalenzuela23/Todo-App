from fastapi import APIRouter, HTTPException, Response, status
from models import User, UserModel
from utils.security import get_password_hash, verify_password

router = APIRouter(prefix="/users")

lista_usuarios: list[UserModel] = []

@router.get("/")
async def get_users():
    return {"users": lista_usuarios}

@router.post("/login")
async def login(response: Response, user: User):

    unauthorize_error = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid credentials", 
                            headers={"WWW-Authenticate": "Bearer"})

    registered_user = [user for user in lista_usuarios if user.name == user.name]
    if not registered_user:
        raise unauthorize_error
    
    model = registered_user[0]

    valid = verify_password(user.password, model.password)

    if (not valid):
        raise unauthorize_error

    response.set_cookie("token", registered_user[0].name)
    #Generate token
    return {"message": "User logged in"}

@router.post("/register")
async def register(user: User):
    if (user.name in [user.name for user in lista_usuarios]):
        return {"message": "User already exists"}
    
    new_user = UserModel(**user.model_dump())
    new_user.password = get_password_hash(new_user.password)
    lista_usuarios.append(new_user)
    
    return {"message": "User registered"}

@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("token")
    return {"message": "User logged out"}

