from fastapi import FastAPI
from app.routers.chat_router import chat_router
from app.routers.product_router import product_router
from app.routers.user_router import user_router
import app.core.chat_config  

app = FastAPI(title="Blog Management API")

app.include_router(chat_router)
app.include_router(product_router)
app.include_router(user_router)


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok"}

