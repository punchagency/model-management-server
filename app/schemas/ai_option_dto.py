from pydantic import BaseModel
from app.schemas.response_dto import ResponseDTO


class BaseAIOptionDTO(BaseModel):
    ai_option: str
    label_name: str


class SimpleAIOptionDTO(BaseAIOptionDTO):
    pass


class AIOptionDTO(BaseAIOptionDTO):
    ai_option_uid: str


class AIOptionCreateDTO(BaseAIOptionDTO):
    pass


class AIOptionUpdateDTO(BaseAIOptionDTO):
    pass


class AIOptionDeleteDTO(BaseModel):
    ai_option_uid: str


class AIOptionGetDTO(BaseModel):
    ai_option_uid: str


class AIOptionGetAllDTO(BaseModel):
    pass
