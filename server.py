import Pyro5.api
import Pyro5.errors
from product import ProductInterface


@Pyro5.api.expose
class ProductImpl(ProductInterface):
    """
    Equivalent to ProductImpl.java & ServerImpl.java.
    Implements the remote Product methods and exposes them via Pyro5.
    """

    def __init__(self, name: str, description: str, price: float):
        self._name = name
        self._description = description
        self._price = price

    def get_name(self) -> str:
        print(f"[SERVER LOG] Remote call received: get_name() -> {self._name}")
        return self._name

    def get_description(self) -> str:
        print(f"[SERVER LOG] Remote call received: get_description() for {self._name}")
        return self._description

    def get_price(self) -> float:
        print(f"[SERVER LOG] Remote call received: get_price() for {self._name}")
        return self._price

    def get_details(self) -> str:
        print(f"[SERVER LOG] Remote call received: get_details() for {self._name}")
        return f"Product: {self._name} | Description: {self._description} | Price: ${self._price:.2f}"


def main():
    # Initialize the Pyro5 Daemon (equivalent to RMI runtime / UnicastRemoteObject)
    daemon = Pyro5.api.Daemon()

    try:
        # Locate the running Pyro5 Name Server (equivalent to LocateRegistry.getRegistry())
        ns = Pyro5.api.locate_ns()
    except Pyro5.errors.NamingError:
        print("[ERROR] Pyro5 Name Server not found!")
        print("Start it first in a separate terminal using: pyro5-ns")
        return

    # Instantiate remote product objects (matching typical JAVA_RMI_IV catalog items)
    laptop = ProductImpl("Laptop", "High-performance developer workstation", 1299.99)
    smartphone = ProductImpl("Smartphone", "5G flagship mobile device", 899.50)

    # Register objects with the Daemon to obtain physical URIs
    uri_laptop = daemon.register(laptop)
    uri_phone = daemon.register(smartphone)

    # Bind logical names in the Name Server (equivalent to Naming.rebind / registry.rebind)
    ns.register("store.product.laptop", uri_laptop)
    ns.register("store.product.smartphone", uri_phone)

    print("==========================================")
    print("Pyro5 Product Server is running...")
    print(f"Registered 'store.product.laptop'     -> {uri_laptop}")
    print(f"Registered 'store.product.smartphone' -> {uri_phone}")
    print("Waiting for client requests (Ctrl+C to stop)...")
    print("==========================================")

    # Enter the server request loop
    daemon.requestLoop()


if __name__ == "__main__":
    main()