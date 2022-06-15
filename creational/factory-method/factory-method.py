from abc import ABC, abstractmethod


class Ticket(ABC):
    """Abstract ticket base class."""

    def __init__(self, customer_name: str, price: float) -> None:
        self.customer_name = customer_name
        self.price = price

    @abstractmethod
    def print_ticket(self):
        """Print ticket"""


class CinemaTicket(Ticket):
    """Cinema ticket."""

    def print_ticket(self):
        print(f"Cinema ticket for {self.customer_name} | Price: {self.price}")


class TheatreTicket(Ticket):
    """Theatre ticket."""

    def print_ticket(self):
        print(f"Theatre ticket for {self.customer_name} | Price: {self.price}")


class Show(ABC):
    """Abstract show. This will create tickets."""

    def __init__(self):
        self.__std_price = 0

    @property
    def ticket_price(self):
        return self.__std_price

    @ticket_price.setter
    def ticket_price(self, price):
        self.__std_price = price

    @abstractmethod
    def create_ticket(self, customer_name: str) -> Ticket:
        """Creates a new ticket."""


class TheatreShow(Show):
    def create_ticket(self, customer_name: str) -> Ticket:
        return TheatreTicket(customer_name, self.ticket_price)


class CinemaShow(Show):
    def create_ticket(self, customer_name: str) -> Ticket:
        return CinemaTicket(customer_name, self.ticket_price)



if __name__ == "__main__":
    show = CinemaShow()
    show.ticket_price = 12.3

    for i in range(10):
        tk = show.create_ticket(f"NAME{i}")
        tk.print_ticket()

    show1 = TheatreShow()
    show1.ticket_price = 22.3

    for i in range(10):
        tk = show1.create_ticket(f"NAME{i}")
        tk.print_ticket()

    show1.ticket_price = 20

    for i in range(10):
        tk = show1.create_ticket(f"NAME{i}")
        tk.print_ticket()