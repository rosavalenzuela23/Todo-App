from fastapi import APIRouter, Response
from models import User, UserModel

router = APIRouter(prefix="/users")

lista_usuarios: list[UserModel] = []

@router.get("/")
async def get_users():
    return {"users": lista_usuarios}

@router.post("/login")
async def login(response: Response, user: User):
    registered_user = [user for user in lista_usuarios if user.name == user.name and user.password == user.password]
    if not registered_user:
        return {"message": "User not found"}

    response.set_cookie("token", registered_user[0].name)
    #Generate token
    return {"message": "User logged in"}

@router.post("/register")
async def register(user: User):
    if (user.name in [user.name for user in lista_usuarios]):
        return {"message": "User already exists"}
    
    new_user = UserModel(**user.model_dump())
    lista_usuarios.append(new_user)
    
    return {"message": "User registered"}

@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("token")
    return {"message": "User logged out"}

