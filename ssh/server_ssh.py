#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket,os
#声明socket类型
server = socket.socket()
#绑定端口
server.bind(('localhost',9999))
#监听
server.listen()

while True:
    conn,addr = server.accept() #等待接收
    print("new conn:",addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行命令：",data)
        cmd_res = os.popen(data.decode()).read()#获取执行结果,也是字符串
        print("before sed",len(cmd_res))
        if len(cmd_res) ==0:
            cmd_res = "cmd has no output..."
        conn.send(str(len(cmd_res.encode())).encode("utf-8")) #先发大小给客户端
        client_ack = conn.recv(1024)
        conn.send(cmd_res.encode('utf-8'))#将数据返回给客户端

server.close()

