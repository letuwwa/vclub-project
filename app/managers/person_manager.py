from app.managers.base_manager import BaseManager
from app.models import Person


class PersonManager(BaseManager):
    model = Person
