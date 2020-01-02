from socket import socket, AF_INET, SOCK_DGRAM

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket(AF_INET, SOCK_DGRAM)
    s.bind ((host, port))

    print('Server started')

    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print(f'Message from: {addr}')
        print(f'From connected user: {data}')
        data = data.upper()
        print(f'Sending: {data}')
        s.sendto(data.encode('utf-8'), addr)

    c.close()

if __name__ == '__main__':
    Main()