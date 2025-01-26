from typing import List
from pydantic import BaseModel


class BaseTestKitDTO(BaseModel):
    test_kit_name: str
    test_kit_description: str
    test_kit_ai_options: List[str]


class TestKitDTO(BaseTestKitDTO):
    test_kit_uid: str
    test_kit_created_at: str
    test_kit_updated_at: str
