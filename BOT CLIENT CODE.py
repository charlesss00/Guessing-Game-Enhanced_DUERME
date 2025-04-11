import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

prompt = client_socket.recv(1024).decode()
print(prompt)
password = "duerme"
client_socket.send(password.encode())

response = client_socket.recv(1024).decode()
print(response)

if "Access granted" not in response:
    client_socket.close()
    exit()

minimum = 1
maximum = 100
guess_count = 0

while minimum <= maximum:
    Guess = (minimum + maximum) // 2
    print(f"Bot guess: {Guess}")
    client_socket.send(str(Guess).encode())
    feedback = client_socket.recv(1024).decode()
    print("Server:", feedback)
    guess_count += 1

    if "Too low" in feedback:
        minimum = Guess + 1
    elif "Too high" in feedback:
        maximum = Guess - 1
    elif "Correct!" in feedback:
        break

client_socket.close()