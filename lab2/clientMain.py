import socket


def main():
    # параметры
    IP, PORT = input("введите IP сервера: "), 6000

    # создание объекта сокета
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # соединение с сервером
    s.connect((IP, PORT))
    while True:
        # отправка сообщения
        text = input(": ")
        s.sendall(text.encode("utf-8"))
        if text == "/esc":
            break

        # прием сообщения
        text = s.recv(1024).decode("utf-8")
        if text == "/esc":
            break
        print(f'сервер: {text}')

    # закрытие сокета
    s.close()


if __name__ == '__main__':
    main()

