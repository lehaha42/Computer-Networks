import socket
import struct
import time


def checksum(source_string):
    sum = 0
    countTo = (len(source_string) // 2) * 2
    count = 0
    while count < countTo:
        thisVal = source_string[count + 1] * 256 + source_string[count]
        sum = sum + thisVal
        sum = sum & 0xffffffff
        count = count + 2
    if countTo < len(source_string):
        sum = sum + source_string[len(source_string) - 1]
        sum = sum & 0xffffffff
    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    data = bytes([0x40]*55)
    header = struct.pack("!BBHHH", 8, 0, 0, 4242, 0)
    header = struct.pack("!BBHHH", 8, 0, checksum(header+data), 64242, 0)
    packet = header + data

    s.sendto(packet, ('127.0.0.1', 0))
    time.sleep(16)
