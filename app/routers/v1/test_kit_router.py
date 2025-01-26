from fastapi import APIRouter

from app.schemas.test_kit_dto import TestKitDTO
router = APIRouter(prefix="/test-kits")


@router.get("/")
def get_test_kits():
    """
    Get all test kits
    """
    return {"message": "Hello, World!"}


@router.post("/")
def add_test_kit(test_kit: TestKitDTO):
    """
    Add a new test kit
    """
    return {"message": "Hello, World!"}


@router.get("/{test_kit_uid}")
def get_test_kit_by_uid(test_kit_uid: str):
    """
    Get a test kit by its uid
    """
    return {"message": "Hello, World!"}


@router.put("/{test_kit_uid}")
def update_test_kit_by_uid(test_kit_uid: str, test_kit: TestKitDTO):
    """
    Update a test kit by its uid
    """
    return {"message": "Hello, World!"}


@router.delete("/{test_kit_uid}")
def delete_test_kit_by_uid(test_kit_uid: str):
    return {"message": "Hello, World!"}
