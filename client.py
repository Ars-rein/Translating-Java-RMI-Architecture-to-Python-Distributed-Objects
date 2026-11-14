import Pyro5.api
import Pyro5.errors


def main():
    print("Connecting to Pyro5 Name Server and looking up remote products...\n")

    try:
        # Create dynamic proxies using PYRONAME URIs (equivalent to Naming.lookup)
        laptop = Pyro5.api.Proxy("PYRONAME:store.product.laptop")
        smartphone = Pyro5.api.Proxy("PYRONAME:store.product.smartphone")

        # Invoke remote methods on the first remote object
        print("--- Remote Object 1 ---")
        print(f"Name        : {laptop.get_name()}")
        print(f"Description : {laptop.get_description()}")
        print(f"Price       : ${laptop.get_price():.2f}")
        print(f"Summary     : {laptop.get_details()}\n")

        # Invoke remote methods on the second remote object
        print("--- Remote Object 2 ---")
        print(f"Name        : {smartphone.get_name()}")
        print(f"Description : {smartphone.get_description()}")
        print(f"Price       : ${smartphone.get_price():.2f}")
        print(f"Summary     : {smartphone.get_details()}\n")

    except Pyro5.errors.NamingError as e:
        print(f"[ERROR] Could not locate remote object in Name Server: {e}")
        print("Ensure 'pyro5-ns' and 'server.py' are both running.")
    except Pyro5.errors.CommunicationError as e:
        print(f"[ERROR] Network communication error with remote server: {e}")


if __name__ == "__main__":
    main()