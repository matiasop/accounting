from pydantic import BaseModel, ConfigDict


class SubcategoryDTO(BaseModel):
    id: int
    category_id: int
    name: str
    model_config = ConfigDict(from_attributes=True)


class SubcategoryInputDTO(BaseModel):
    name: str
