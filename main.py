from datetime import date

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

birthdays: dict[str, date] = {
    "Ben": date(year=1982, month=8, day=1),
    "Katya": date(year=1985, month=6, day=15),
}


@app.get("/")
def root() -> dict[str, str]:
    """The stuff with the things."""
    return {"stuff": "things"}


@app.get("/birthdays")
def get_birthdays() -> dict[str, date]:
    """Get all birthdays."""
    return birthdays


class BirthdayInfo(BaseModel):
    """Name-birthday pairs."""

    name: str
    """The name."""
    date: date
    """The date."""


@app.get("/birthdays/{name}")
def get_birthday_info_by_name(name: str) -> BirthdayInfo:
    """Get info by the name.

    Args:
        name (str): the name

    Raises:
        HTTPException: no info found for `name`

    Returns:
        BirthdayInfo: the info
    """
    if name not in birthdays:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return BirthdayInfo(name=name, date=birthdays[name])


@app.put("/birthday")
def put_birthday_info(info: BirthdayInfo):
    """Add or update birthday info.

    Args:
        info (BirthdayInfo): the info
    """
    birthdays[info.name] = info.date
