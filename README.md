# PYTHON_RMI_LAB (Java RMI to Pyro5 Translation)

This project translates a multi-file Java Remote Method Invocation (`JAVA_RMI_IV`) distributed system into an equivalent Python distributed system using **Pyro5 (Python Remote Objects)**.

 Project Structure


PYTHON_RMI_LAB/
│
├── product.py   # Equivalent to Product.java (Remote Interface definition)
├── server.py    # Equivalent to ProductImpl.java, ServerImpl.java, and Server.java
├── client.py    # Equivalent to Client.java
└── README.md    # Setup and execution instructions

## Step-by-Step Setup & Execution Guide

### Phase 1: Project Setup

1. Create the project directory and navigate into it:
   ```bash
   cd PYTHON_RMI_LAB
   ```

2. Install the Pyro5 library using your active Python interpreter:
   ```bash
   python -m pip install Pyro5
   ```


### STEPS

Open three separate terminal windows inside the `PYTHON_RMI_LAB/` directory and run the following commands in order:

1.Terminal 1 — Start the Pyro5 Name Server (replaces Java `rmiregistry`):
   ```bash
   python -m Pyro5.nameserver
   ```
   *Wait until `NS running on localhost:9090` appears. Keep this terminal open.*

2. Terminal 2 — Start the Remote Object Server:
   ```bash
   python server.py
   ```
   *Wait until `Pyro5 Product Server is running...` appears. Keep this terminal open.*

3. Terminal 3 — Run the Client:
   ```bash
   python client.py
   ```
   *The client will connect to the Name Server, look up the remote `ProductImpl` objects, and display their details while logging requests on the server terminal.*

---

