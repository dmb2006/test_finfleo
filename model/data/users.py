from dataclasses import dataclass

@dataclass()
class Submit_user:
    name = 'Test'
    phone = '95212345678'


@dataclass()
class Basket_user:
    name: str
    phone: str
    email: str
    address: str