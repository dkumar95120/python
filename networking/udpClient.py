from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname

def Main():
    host = '127.0.0.1'
    port = 5001

    server = (gethostbyname("localhost"), 5000)
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind((host, port))

    message = input('-> ')

    while message != 'q':
        s.sendto (message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)

        data = data.decode('utf-8')
        print(f'Received from server: {data}')
        message = input('-> ')

    s.close()

if __name__ == '__main__':
    Main()