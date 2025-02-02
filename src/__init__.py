from fastapi import FastAPI
from src.books.routes import router as books_router
from src.users.routes import router as users_router
from contextlib import asynccontextmanager
from src.db.main import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"welcome to APi its started now")
    await init_db()
    yield
    print(f"Bye bye API its stopped now")

version = "v1"
app = FastAPI(
    version= version,
    title="Book API",
    description="A simple API to manage books",
    lifespan= life_span
)

app.include_router(books_router, prefix=f"/api/{version}/books", tags=["Books"])
app.include_router(users_router, prefix=f"/api/{version}/user", tags=["Users"]) 
