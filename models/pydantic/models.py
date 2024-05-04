from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, computed_field
from dateutil.relativedelta import relativedelta


class AnimalCreate(BaseModel):
    animal_type: str
    name: str
    birth_date: date
    breed: str
    photo_url: str


class AnimalResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    animal_type: str
    name: str
    birth_date: date
    breed: str
    photo_url: str

    @computed_field
    @property
    def age(self) -> int:
        return relativedelta(datetime.now(), self.birth_date).years
