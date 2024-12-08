import socket


def main():
    # параметры
    IP, PORT = input("введите IP сервера: "), 6000

    # создание объекта сокета
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # отправка сообщения
        text = input(": ")
        s.sendto(text.encode("utf-8"), (IP, PORT))
        if text == "/esc":
            break

        # прием сообщения
        data, _ = s.recvfrom(1024)
        text = data.decode('utf-8')
        if text == "/esc":
            break
        print(f'сервер: {text}')

    # закрытие сокета
    s.close()


if __name__ == '__main__':
    main()
