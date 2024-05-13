import socket

host = "localhost"
port = 5555

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running.")
        exit()

    try:
        data = s.recv(1024)
        print(data.decode().strip())
        difficulty_choice = input("")
        s.sendall(difficulty_choice.encode())

        while True:
            user_input = input("").strip()
            s.sendall(user_input.encode())
            reply = s.recv(1024).decode().strip()
            if "Correct" in reply:
                print(reply)
                name = input("Enter your name: ")
                s.sendall(name.encode())
                s.sendall(difficulty_choice.encode())
                break
            print(reply)
            continue
    except Exception as e:
        print("An error occurred:", e)
    finally:
        s.close()

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break
