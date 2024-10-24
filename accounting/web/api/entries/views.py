from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends

from accounting.db.dao.accounts_dao import AccountDAO
from accounting.db.dao.entries_dao import EntryDAO
from accounting.db.models.entries import Entry
from accounting.web.api.entries.schema import EntryDTO, EntryInputDTO

router = APIRouter()


@router.get("/", response_model=list[EntryDTO])
async def get_entries(entry_dao: EntryDAO = Depends()) -> list[Entry]:
    return await entry_dao.get_all()


@router.get("/{entry_id}", response_model=EntryDTO)
async def get_entry_by_id(
    entry_id: int,
    entry_dao: EntryDAO = Depends(),
) -> Entry | None:
    entry = await entry_dao.get_by_id(entry_id)

    if entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")

    return entry[0]


@router.post("/", response_model=EntryDTO, status_code=201)
async def create_entry(
    new_entry_object: EntryInputDTO,
    entry_dao: EntryDAO = Depends(),
    account_dao: AccountDAO = Depends(),
) -> Entry:
    credit_account = await account_dao.get_by_id(new_entry_object.credit_account_id)
    if credit_account is None:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid credit_account_id provided ({new_entry_object.credit_account_id}), credit account does not exist",
        )
    debit_account = await account_dao.get_by_id(new_entry_object.debit_account_id)
    if debit_account is None:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid debit_account_id provided ({new_entry_object.debit_account_id}), debit account does not exist",
        )
    entry = await entry_dao.create(
        description=new_entry_object.description,
        type=new_entry_object.type,
        datetime=new_entry_object.datetime,
        category=new_entry_object.category,
        subcategory=new_entry_object.subcategory,
        debit=new_entry_object.debit,
        credit=new_entry_object.credit,
        credit_account_id=new_entry_object.credit_account_id,
        debit_account_id=new_entry_object.debit_account_id,
    )
    if entry is None:
        raise HTTPException(status_code=500, detail="Failed to create entry")

    return entry
