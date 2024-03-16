import os
import sys
import socket, threading

EXIT = threading.Event()


def kill_client() -> None:
    os.system('ps -aux > /home/imcocos/.processes.tmp')

    with open('/home/student/rofler/.processes.tmp', 'r') as file:
        processes = file.read().strip().split('\n')[1:]

    for process in processes:
        if 'client.py' in process:
            pid = process.split()[1]
            os.system(f'kill QUIT {pid} > /dev/null 2> /dev/null')


def handle_messages(connection: socket.socket):
    '''
        Receive messages sent by the server and display them to user
    '''

    while True:
        try:
            msg = connection.recv(1024)

            # If there is no message, there is a chance that connection has closed
            # so the connection will be closed and an error will be displayed.
            # If not, it will try to decode message in order to show to user.
            if msg and msg.decode() != 'break':
                print(f'417(^-^): {msg.decode()}')
            else:
                kill_client()
                EXIT.set()
                connection.close()
                break

        except Exception as e:
            print(f'ERR 1 - {e}')
            print(f'Error handling message from server: {e}')
            connection.close()
            break

def client() -> None:
    '''
        Main process that start client connection to the server 
        and handle it's input messages
    '''

    SERVER_ADDRESS = sys.argv[1]
    SERVER_PORT = int(sys.argv[2])

    try:
        # Instantiate socket and start connection with server
        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
        # Create a thread in order to handle messages sent by server
        handler_thread = threading.Thread(target=handle_messages, args=[socket_instance])
        handler_thread.start()

        print('Hey, looser, your PC was hacked!')

        # Read user's input until it quit from chat and close connection
        while True:
            msg = input()
            if EXIT.is_set():
                break
            # Parse message to utf-8
            socket_instance.send(msg.encode())

        # Close connection with the server
        socket_instance.close()

    except Exception as e:
        print(f'ERR 1 - {e}')
        print(f'Error connecting to server socket {e}')
        socket_instance.close()


if __name__ == "__main__":
    client()
