from datetime import date
from typing import Literal

from dash_pydantic_form import ModelForm
from pydantic import BaseModel, Field


class Address(BaseModel):
    street_address: str = Field(title="Street address")
    city: str = Field(title="City")
    postcode: str = Field(title="Postcode")
    country: str = Field(title="Country")


class Hobby(BaseModel):
    name: str = Field(title="Hobby")
    started_on: date = Field(title="Started on")


class Cat(BaseModel):
    species: Literal["cat"]
    meows: bool = True


class Dog(BaseModel):
    species: Literal["dog"]
    barks: bool = True


class Person(BaseModel):
    name: str = Field(title="Full name")
    address: Address = Field(title="Address")
    hobbies: list[Hobby] = Field(title="Hobbies", default_factory=list)
    pet: Cat | Dog | None = Field(title="Pet", discriminator="species", default=None)


component = ModelForm(Person, "person", "new_person")
