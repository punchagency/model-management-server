from fastapi import APIRouter

router = APIRouter(prefix="/v1")


@router.get("/")
def read_root():
    return {"message": "Welcome to the Punch Model Management Server"}
