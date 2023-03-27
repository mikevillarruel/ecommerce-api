from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.application.controllers import users_router, products_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=users_router, prefix="/api/users")
app.include_router(router=products_router, prefix="/api/products")
