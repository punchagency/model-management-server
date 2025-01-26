from fastapi import APIRouter
from app.routers.v1.ai_option_router import router as ai_option_router
from app.routers.v1.test_kit_router import router as test_kit_router

router = APIRouter(prefix="/v1")

router.include_router(ai_option_router)
router.include_router(test_kit_router)


@router.get("/")
def read_root():
    return {"message": "Welcome to the Punch Model Management Server"}
