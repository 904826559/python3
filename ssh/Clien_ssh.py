#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
#声明类型
clien = socket.socket()
#连接
clien.connect(("localhost",9999))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:continue
    clien.send(cmd.encode("utf-8"))
    cmd_res_size = clien.recv(1024)#接受命令的结果长度
    print("命令结果大小：",cmd_res_size)
    client.send("准备好接受了，loser可以发了".encode("utf-8"))
    receivd_size = 0
    receivd_data = b''
    while receivd_size < int(cmd_res_size.decode()):
        data = clien.recv(1024)
        receivd_size += len(data) #每次收到的有可能小于1024，所以必须用len判断
        receivd_data += data #接收服务端返回的数据
    else:
        print("cmd res ...",receivd_size)
        print(receivd_data.decode())#打印服务端返回的数据

clien.close()