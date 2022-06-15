"""The abstract factory pattern is used when you want to separate the creation 
of object from client code. It is often used when you have multiple products that 
needs to be created by the same factory. EX: you have notebooks, pens and hoodies
as products and you have to create custom branded products for different companies.
So you have the products that behave the same for any company but look different
due to customization. The relation between products is that they will have the 
same logo."""
from abc import ABC, abstractmethod
from enum import Enum


class HoodieSize(Enum):
    """Hoodie size."""

    XS = 0
    S = 1
    M = 2
    L = 3
    XL = 4
    XXL = 5


class Product(ABC):
    """Generic product."""

    @abstractmethod
    def purchase(self) -> None:
        """Buy a new notebook."""

    @abstractmethod
    def get_brand_name(self) -> str:
        """Show brand name"""


# Abstract products
class Notebook(Product):
    """Generic notebook."""

    @abstractmethod
    def get_pages(self) -> int:
        """Get the number of pages."""


class Pen(Product):
    """Generic pen."""


class Hoodie(Product):
    """Generic hoodie."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_size(self) -> HoodieSize:
        """Get hoodie size."""


# Concrete products
class EndavaNotebook(Notebook):
    """Custom Endava branded notebook."""

    def __init__(self) -> None:
        super().__init__()
        self.__pages = 50

    def purchase(self):
        print(f"You purchased a new {self.get_brand_name()} notebook.")

    def get_brand_name(self):
        return "Endava"

    def get_pages(self) -> int:
        return self.__pages


class EndavaPen(Pen):
    """Custom Endava pen."""

    def purchase(self) -> None:
        print(f"You purchased a new {self.get_brand_name()} pen.")

    def get_brand_name(self) -> str:
        return "Endava"


class EndavaHoodie(Hoodie):
    """Custom Endava hoodie."""

    def __init__(self, size: HoodieSize) -> None:
        self.__size = size
        super().__init__()

    def purchase(self) -> None:
        print(f"You purchased a new {self.get_brand_name()} hoodie.")

    def get_brand_name(self) -> str:
        return "Endava"

    def get_size(self) -> HoodieSize:
        return self.__size


class HarmanNotebook(Notebook):
    """Custom Harman branded notebook."""

    def __init__(self) -> None:
        super().__init__()
        self.__pages = 100

    def purchase(self):
        print(f"You purchased a new {self.get_brand_name()} notebook.")

    def get_brand_name(self):
        return "Harman"

    def get_pages(self) -> int:
        return self.__pages


class HarmanPen(Pen):
    """Custom Harman pen."""

    def purchase(self) -> None:
        print(f"You purchased a new {self.get_brand_name()} pen.")

    def get_brand_name(self) -> str:
        return "Harman"


class HarmanHoodie(Hoodie):
    """Custom Harman hoodie."""

    def __init__(self, size: HoodieSize) -> None:
        super().__init__()
        self.__size = size

    def purchase(self) -> None:
        print(f"You purchased a new {self.get_brand_name()} hoodie.")

    def get_brand_name(self) -> str:
        return "Harman"

    def get_size(self) -> HoodieSize:
        return self.__size


# Abstract factory
class Factory(ABC):
    """Generic factory."""

    @abstractmethod
    def create_notebook(self) -> Notebook:
        """Get generic notebook."""

    @abstractmethod
    def create_pen(self) -> Pen:
        """Get generic pen."""

    @abstractmethod
    def create_hoodie(self, size) -> Hoodie:
        """Get generic hoodie."""


# Concrete factories
class EndavaFactory(Factory):
    """Endava branded factory."""

    def create_notebook(self) -> Notebook:
        return EndavaNotebook()

    def create_pen(self) -> Pen:
        return EndavaPen()

    def create_hoodie(self, size) -> Hoodie:
        return EndavaHoodie(size)


class HarmanFactory(Factory):
    """Harman branded factory."""

    def create_notebook(self) -> Notebook:
        return HarmanNotebook()

    def create_pen(self) -> Pen:
        return HarmanPen()

    def create_hoodie(self, size) -> Hoodie:
        return HarmanHoodie(size)


def get_factories() -> dict:
    """Get factory by brand name."""
    return {"harman": HarmanFactory, "endava": EndavaFactory}


def input_brand():
    """Get user input. Run in loop until one of available option is chosen."""
    choices = get_factories().keys()
    inp = input(f"Select brand. Choices: {','.join(choices)} >")

    if inp not in choices:
        print("Please chose from available choices.")
        input_brand()

    return inp

def create_factory(_brand) -> Factory:
    """Create a new factory instance depending on brand."""
    return get_factories().get(_brand)()

# Client code
if __name__ == "__main__":
    brand = input_brand()
    factory = create_factory(brand)
    factory.create_hoodie(HoodieSize.M).purchase()
    factory.create_notebook().purchase()
    factory.create_pen().purchase()
