# coding: utf-8
# 实现数据管理功能的主要类


class DataBaseManager(object):
    pass


class COLDManager(object):
    def __init__(self):
        self.file_root = "Item"
        self.template_file_root = "Template"
        self.xml_file_root = "XML"
        self.script_file_root = "script"

    def get_item(self, item_addr):
        #
        # 查询文件
        try:
            if item_addr == "/":
                with open("Item/Template/" + "home.html", 'r') as file:

                    temp_file = file.readlines()
                    ret_file = ""
                    for line in temp_file:
                        ret_file += line
            else:
                item_addr = self.file_root + item_addr
                with open(item_addr, 'r') as file:
                    temp_file = file.readlines()
                    ret_file = ""
                    for line in temp_file:
                        ret_file += line

            return ret_file

        except IOError as ioe:
            return None
