from pydantic import BaseModel


class CategoryDTO(BaseModel):
    id: int
    name: str
    # model_config = ConfigDict(from_attributes=True)


class CategoryInputDTO(BaseModel):
    """DTO for creating new category"""

    name: str
