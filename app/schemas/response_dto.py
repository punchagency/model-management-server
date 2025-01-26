from pydantic import BaseModel


class ResponseDTO(BaseModel):
    status: str
    message: str
    data: BaseModel | None = None
    error: str | None = None
    status_code: int

    def __init__(self, status: str, message: str, data: BaseModel | None, error: str | None, status_code: int):
        self.status = status
        self.message = message
        self.data = data
        self.error = error
        self.status_code = status_code


class SuccessResponseDTO(ResponseDTO):
    status: str = "success"
    status_code: int = 200


class ErrorResponseDTO(ResponseDTO):
    status: str = "error"
    status_code: int = 400


class NotFoundResponseDTO(ErrorResponseDTO):
    status_code: int = 404
    message: str = "Not Found"
