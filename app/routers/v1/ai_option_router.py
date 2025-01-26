from fastapi import APIRouter

from app.schemas.ai_option_dto import AIOptionCreateDTO, BaseAIOptionDTO

router = APIRouter(prefix="/ai-options")


@router.get("/")
def get_ai_options():
    return {"message": "Hello, World!"}


@router.post("/")
def add_ai_option(ai_option: AIOptionCreateDTO):
    return {"message": "Hello, World!"}


@router.get("/{ai_option_uid}")
def get_ai_option_by_uid(ai_option_uid: str):
    return {"message": "Hello, World!"}


@router.put("/{ai_option_uid}")
def update_ai_option_by_uid(ai_option_uid: str, ai_option: BaseAIOptionDTO):
    return {"message": "Hello, World!"}


@router.delete("/{ai_option_uid}")
def delete_ai_option_by_uid(ai_option_uid: str):
    return {"message": "Hello, World!"}
