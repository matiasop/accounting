from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends

from accounting.db.dao.subcategories_dao import SubcategoryDAO
from accounting.db.models.subcategories import Subcategory
from accounting.web.api.subcategories.schema import SubcategoryDTO

router = APIRouter()


@router.get("/", response_model=list[SubcategoryDTO])
async def get_subcategories(
    subcategory_dao: SubcategoryDAO = Depends(),
) -> list[Subcategory]:
    return await subcategory_dao.get_all()


@router.get("/{subcategory_id}", response_model=SubcategoryDTO)
async def get_subcategory_by_id(
    subcategory_id: int,
    subcategory_dao: SubcategoryDAO = Depends(),
) -> Subcategory:
    subcategory = await subcategory_dao.get_by_id(subcategory_id)

    if subcategory is None:
        raise HTTPException(status_code=400, detail="Subcategory not found")

    return subcategory
