from fastapi import FastAPI
from src.books.routes import router as books_router
version = "v1"
app = FastAPI(
    version= version,
    title="Book API",
    description="A simple API to manage books"
)

app.include_router(books_router, prefix=f"/api/{version}/books", tags=["Books"])
