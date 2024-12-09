import socket


def main():
    # параметры
    sIP, sPORT = '127.0.0.2', 6001

    # создание объекта сокета
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # создание сервера с IP и портом
    s.bind((sIP, sPORT))

    while True:
        # прием сообщения
        data, (cIP, cPORT) = s.recvfrom(1024)
        text = data.decode('utf-8')
        if text == '/esc':
            break
        print(f'{cIP}: {text}')

        # отправка сообщения
        text = input(": ")
        s.sendto(text.encode("utf-8"), (cIP, cPORT))
        if text == '/esc':
            break

    # закрытие сокета
    s.close()


if __name__ == '__main__':
    main()
