import socket


def main():
    # параметры
    IP, PORT = '255.255.255.255', int(input('введите порт сервера: '))

    # создание объекта сокета
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # настройка широковещания
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # настройка таймаута
    s.settimeout(10)
    running = True

    while running:
        # отправка сообщения
        text = input(": ")
        s.sendto(text.encode("utf-8"), (IP, PORT))
        if text == "/esc":
            break

        # прием сообщения
        while running:
            try:
                data, serv = s.recvfrom(1024)
                text = data.decode('utf-8')
                if text == "/esc":
                    s.sendto('/esc'.encode("utf-8"), (IP, PORT))
                    running = False
                    break
                print(f'{serv[0]}:{serv[1]} :: {text}')
            except socket.timeout:
                print('время истекло')
                break

    # закрытие сокета
    s.close()


if __name__ == '__main__':
    main()
