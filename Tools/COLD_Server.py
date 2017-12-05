# coding: utf-8
# 实现接受链接的主线程

import socket
import COLD_Choose


class COLDServer(object):
    def __init__(self, max_clients=500, ip='0.0.0.0', port=80):
        self.name = "COLD"
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip, port))
        self.max_clients = max_clients
        self.client_count = 0

    def access_connection(self):
        sock, addr = self.server_socket.accept()
        try:
            COLD_Choose.COOLServer(sock, addr).start()
        except Exception as e:
            print(e)
            print("\nToo many threads.")

    def refuse_connection(self):
        sock, addr = self.server_socket.accept()
        ########
        # send sorry here
        ########
        sock.close()

    def service(self):
        self.server_socket.listen(self.max_clients)
        while True:
            if self.client_count < self.max_clients - 1:  # 保留一个控制接口
                self.access_connection()
            else:
                self.refuse_connection()


if __name__ == "__main__":
    server = COLDServer(ip='0.0.0.0', port=80)
    server.service()
