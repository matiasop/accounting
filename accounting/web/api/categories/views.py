from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends

from accounting.db.dao.categories_dao import CategoryDAO
from accounting.db.dao.subcategories_dao import SubcategoryDAO
from accounting.db.models.categories import Category
from accounting.db.models.subcategories import Subcategory
from accounting.web.api.categories.schema import CategoryDTO, CategoryInputDTO
from accounting.web.api.subcategories.schema import SubcategoryDTO, SubcategoryInputDTO

router = APIRouter()


@router.get("/", response_model=list[CategoryDTO])
async def get_categories(category_dao: CategoryDAO = Depends()) -> list[Category]:
    return await category_dao.get_all()


@router.get("/{category_id}", response_model=CategoryDTO)
async def get_category_by_id(
    category_id: int,
    category_dao: CategoryDAO = Depends(),
) -> Category:
    category = await category_dao.get_by_id(category_id)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@router.get("/{category_id}/subcategories", response_model=list[SubcategoryDTO])
async def get_subcategories_by_category_id(
    category_id: int,
    category_dao: CategoryDAO = Depends(),
) -> list[Subcategory]:
    subcategories = await category_dao.get_subcategories_by_category_id(category_id)
    return subcategories


@router.post("/", response_model=CategoryDTO, status_code=201)
async def create_category(
    new_category_object: CategoryInputDTO,
    category_dao: CategoryDAO = Depends(),
) -> Category:
    category = await category_dao.create(name=new_category_object.name)

    if category is None:
        raise HTTPException(status_code=500, detail="Failed to create category")

    return category


@router.post(
    "/{category_id}/subcategories",
    response_model=SubcategoryDTO,
    status_code=201,
)
async def create_subcategory(
    category_id: int,
    new_subcategory_object: SubcategoryInputDTO,
    category_dao: CategoryDAO = Depends(),
    subcategory_dao: SubcategoryDAO = Depends(),
) -> Subcategory:
    category = await category_dao.get_by_id(category_id)
    if category is None:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid category id provided ({category_id}), category does not exist",
        )

    subcategory = await subcategory_dao.create(
        name=new_subcategory_object.name,
        category_id=category_id,
    )

    if subcategory is None:
        raise HTTPException(status_code=500, detail="Failed to create subcategory")

    return subcategory
