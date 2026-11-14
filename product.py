from abc import ABC, abstractmethod


class ProductInterface(ABC):
    """
    Equivalent to Product.java (Remote Interface).
    Defines the contract of methods exposed by remote Product objects.
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def get_details(self) -> str:
        pass