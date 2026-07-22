from fastapi import FastAPI

from app.routers.user_router import user_router


app = FastAPI(title="User CRUD")
app.include_router(user_router)


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok"}
