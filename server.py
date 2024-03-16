import sys
import socket, threading

# Global variable that mantain client's connections
CONNECTION: socket.socket = None

def handle_user_connection(connection: socket.socket, address: str) -> None:
    '''
        Get user connection in order to keep receiving their messages and
        sent to others users/connections.
    '''
    while True:
        try:
            # Get client message
            msg = connection.recv(1024)

            # If no message is received, there is a chance that connection has ended
            # so in this case, we need to close connection and remove it from connections list.
            if msg:
                # Log message sent by user
                print(f'{address[0]}:{address[1]} - {msg.decode()}')
            # Close connection if no message was sent
            else:
                remove_connection(connection)
                break

        except Exception as e:
            print(f'Error to handle user connection: {e}')
            remove_connection(connection)
            break


def remove_connection(conn: socket.socket) -> None:
    '''
        Remove specified connection from connections list
    '''

    # Check if connection exists on connections list
    # Close socket connection and remove connection from connections list
    global CONNECTION
    if conn:
        conn.close()
    CONNECTION = None

def server() -> None:
    '''
        Main process that receive client's connections and start a new thread
        to handle their messages
    '''

    LISTENING_PORT = int(sys.argv[1])
    global CONNECTION
    
    try:
        # Create server and specifying that it can only handle 4 connections by time!
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.bind(('', LISTENING_PORT))
        socket_instance.listen(4)

        print(f'Server running on port {LISTENING_PORT}')
        
        while True:

            # Accept client connection
            if not CONNECTION:
                socket_connection, address = socket_instance.accept()
                # Add client connection to connections list
                CONNECTION = socket_connection
                # Start a new thread to handle client connection and receive it's messages
                # in order to send to others connections
                threading.Thread(target=handle_user_connection, args=[socket_connection, address]).start()
            else:
                msg = input()
                if msg:
                    socket_connection.send(f'Hacker: {msg}'.encode())

    except Exception as e:
        print(f'An error has occurred when instancing socket: {e}')
    finally:
        # In case of any problem we clean all connections and close the server connection
        remove_connection(CONNECTION)
        socket_instance.close()


if __name__ == "__main__":
    server()
