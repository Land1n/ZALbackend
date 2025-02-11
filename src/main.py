from fastapi import FastAPI
import uvicorn


from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemes import UserCreate,UserRead


app = FastAPI(
    title="ZAL"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)
