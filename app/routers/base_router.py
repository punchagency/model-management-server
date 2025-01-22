from fastapi import APIRouter
from app.routers.v1.root import router as root_router

router = APIRouter(prefix="/api")


router.include_router(root_router)
