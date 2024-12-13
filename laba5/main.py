import socket
import struct
import time
import os


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


def create_packet():
    data = bytes([0x42] * 42)
    id = os.getpid() & 0xFFFF
    header = struct.pack("!BBHHH", 8, 0, 0, id, 0)
    header = struct.pack("!BBHHH", 8, 0, checksum(header + data), id, 0)
    return header + data


def traceroute(ip, max_ttl, timeout):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    packet = create_packet()
    s.settimeout(timeout)
    for i in range(max_ttl):
        s.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, i+1)
        s.sendto(packet, (ip, 0))
        try:
            start = time.time()
            res, ret_ip = s.recvfrom(4096)
            dif = (time.time() - start)*1000.
            print(f'{i+1}\t{dif:.2f}ms\t{ret_ip[0]}')
            if ret_ip[0] == ip:
                break
        except TimeoutError:
            print(f'{i+1}\t  *   \ttime out')


def main():
    inp = input(': ').split(' ')
    max_ttl = 30
    timeout = 3
    if len(inp) > 2:
        timeout = int(inp[2])
    if len(inp) > 1:
        max_ttl = int(inp[1])
    traceroute(inp[0], max_ttl, timeout)


if __name__ == '__main__':
    main()
