from fastapi.routing import APIRouter

from accounting.web.api import (
    accounts,
    categories,
    dummy,
    echo,
    entries,
    monitoring,
    subcategories,
    users,
)

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(users.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
api_router.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(
    subcategories.router,
    prefix="/subcategories",
    tags=["subcategories"],
)
api_router.include_router(entries.router, prefix="/entries", tags=["entries"])
