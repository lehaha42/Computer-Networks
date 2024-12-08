import socket


def main():
    # параметры
    sIP, sPORT = '0.0.0.0', 6000

    # создание объекта сокета
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # создание сервера с IP и портом
    s.bind((sIP, sPORT))
    s.listen()

    # получение клиента
    client, (clIP, clPORT) = s.accept()

    # вывод информации о клиенте
    print(f'подключен {clIP} с портом {clPORT}')
    while True:
        # прием сообщения
        text = client.recv(1024).decode("utf-8")
        print(f'{clIP}: {text}')
        if text == '/esc':
            break

        # отправка сообщения
        text = input(": ")
        client.sendall(text.encode("utf-8"))
        if text == '/esc':
            break

    # закрытие сокета
    s.close()


if __name__ == '__main__':
    main()
