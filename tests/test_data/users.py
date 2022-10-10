from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History: str = 'History'
    Maths: str = 'Maths'
    Physics: str = 'Physics'


class Hobby(Enum):
    Sports: str = 'Sports'
    Reading: str = 'Reading'
    Music: str = 'Music'


class Gender(Enum):
    Male: str = 'Male'
    Female: str = 'Female'
    Other: str = 'Other'


@dataclass
class User:
    gender: Gender
    name: str
    last_name: str = 'Romanova'
    email: str = 'elena@mail.ru'
    mobile: str = '1234567891'
    birth_day: str = '30'
    birth_month: str = 'March'
    birth_year: str = '1995'
    subjects: Tuple[Subject] = (Subject.History, Subject.Maths, )
    hobbies: Tuple[Hobby] = (Hobby.Sports, Hobby.Reading)
    current_address: str = 'Astana'
    picture_file: str = 'photo.jpg'
    state: str = 'Haryana'
    city: str = 'Karnal'


user = User(name='Elena', gender=Gender.Female)
