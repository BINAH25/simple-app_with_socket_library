# simple-app_with_socket_library

This project demonstrates basic socket communication between a client and a server using Python's built-in socket module. The client sends a message to the server, and the server responds with the same message back to the client.

## Files Overview

1. **client.py**: Contains the client-side code, which sends a message to the server and waits for the server's response.
2. **server.py**: Contains the server-side code, which listens for incoming client connections, receives messages, and sends them back.

## Running the Server
1. Open a terminal/command prompt.
2. Navigate to the directory where the server.py script is located.
3. Run the server script:

    ```bash
        python3 server.py

    The server will start listening on 127.0.0.1 (localhost) and port 12345. It will wait for a client to connect.


## Running the lient
1. Open a terminal/command prompt.
2. Navigate to the directory where the client.py script is located.
3. Run the client script:

    ```bash
        python3 client.py

    The client will connect to the server, send the message "Hello Server", and print the server's response (which will be the same message it received).

