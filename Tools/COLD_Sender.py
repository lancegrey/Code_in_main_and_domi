# coding: utf-8
# 实现发送数据给客户端
import COLD_Manager


class CLODSender(object):
    def __init__(self, sock):
        self.sock = sock
        self.manager = COLD_Manager.COLDManager()
        self.GET_heder = "HTTP/1.1 200 OK\r\n"
        self.GET_heder += "Date:Mon, 31 Dec 200104:25:57 GMT\r\n"
        self.GET_heder += "Server:LANCE_COLD/0.00.000\r\n"
        self.GET_heder += "Content-type:text/html\r\n"
        self.GET_heder += "Content-Charset:utf-8\r\n"
        self.GET_heder += "Last-modified:None\r\n"

    @staticmethod
    def add_length(bdata):
        return "Content-Length:" + str(len(bdata)) + "\r\n"

    def send(self, action):
        item_addr = action["url"]
        msg = self.manager.get_item(item_addr)
        if msg is not None:
            #
            # 这里完成msg的包装
            if action['method'] == 'GET':
                msg = self.GET_heder + self.add_length(msg.encode()) + "\n" + msg
            #
            msg = msg.encode()
            self.sock.sendall(msg)
        else:
            self.sock.sendall("HTTP/1.1 404 \r\n".encode())

    def post(self, action):
        pass

