from fastapi import APIRouter
from fastapi.param_functions import Depends

from accounting.db.dao.accounts_dao import AccountDAO
from accounting.db.models.accounts import Account
from accounting.web.api.accounts.schema import AccountDTO, AccountInputDTO

router = APIRouter()


@router.get("/", response_model=list[AccountDTO])
async def get_accounts(account_dao: AccountDAO = Depends()) -> list[Account]:
    return await account_dao.get_all()


@router.post("/")
async def create_account(
    new_account_object: AccountInputDTO,
    account_dao: AccountDAO = Depends(),
) -> None:
    await account_dao.create(
        name=new_account_object.name,
        type=new_account_object.type,
        initial_amount=new_account_object.initial_amount,
    )
