from fastapi import FastAPI
from controllers.book_controller import router as book_router

app = FastAPI(title="Library Book Mock API")

app.include_router(book_router, prefix="/api", tags=["Books"])
