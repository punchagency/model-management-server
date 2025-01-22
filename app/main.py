from fastapi import FastAPI
import uvicorn
from app.routers.base_router import router as base_router
app = FastAPI(
    title="Model Management Server",
    description="Server for managing models",
    version="1.0.0",
    summary="Server for managing models",
    contact={
        "name": "Punch LLC",
        "url": "https://punch.ai",
        "email": "contact@punch.ai",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(base_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Punch Model Management Server"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
