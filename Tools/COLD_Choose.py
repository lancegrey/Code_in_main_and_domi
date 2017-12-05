# coding: utf-8
# 实现判断所有客户端请求并传递
import threading
import socket
import COLD_Sender
import re


class COLDChooser(object):
    def __init__(self, sock, addr):
        self.addr = addr
        self.sock = sock
        self.connect = True
        self._is_GET = re.compile(r"GET")
        self._is_POST = re.compile(r"POST")
        self._agent = re.compile(r"User-Agent:")

    def choose_action(self):
        rev = self.sock.recv(128).decode()
        if rev is None:
            self.connect = False
            return None
        else:
            try:
                #
                # 这里生成字典http字符信息字典
                ret_dict = {}
                rev_list = rev.splitlines()
                split_list = rev_list[0].split(" ")
                ret_dict['method'] = split_list[0]
                if self._is_GET.match(ret_dict['method']) is not None:
                    method, url, http_version = split_list
                    ret_dict['url'] = url
                    ret_dict['http_version'] = http_version

                elif self._is_POST.match(ret_dict['method']) is not None:
                    #
                    # 这里完成post
                    #
                    pass

                else:

                    pass

            except IndexError as e:
                self.connect = False
                return None
            except KeyError as e:
                self.connect = False
                return None

            #
            return ret_dict


class COOLServer(threading.Thread):
    def __init__(self, sock, addr):
        super(COOLServer, self).__init__()
        #
        # 这里添加判断ip等功能
        #
        self.sock = sock
        self.addr = addr

    def run(self):
        chooser = COLDChooser(sock=self.sock, addr=self.addr)
        sender = COLD_Sender.CLODSender(sock=self.sock)
        while True:
            action = chooser.choose_action()
            if action is None or not chooser.connect:
                self.sock.close()
                break
            else:
                if action["method"] == "GET":
                    sender.send(action)
                elif action["method"] == "POST":
                    sender.post(action)

        self.sock.close()

if __name__ == "__main__":
    sersock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sersock.bind(("127.0.0.1", 58945))
    sersock.listen()
    so, ad = sersock.accept()

    COOLServer(so, ad).start()

