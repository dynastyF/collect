# _*_coding:utf-8_*_

import platform #识别运行环境的操作系统
import uuid #通用唯一标识符，通过mac,时间戳，命名空间，随机数，伪随数，128位
import time #时间获取和转换 ；时间戳：从1970.1.1按秒计算的偏移量；utc 格林威治天文时间；dst:夏令时
import socket #python的套接字通信模块 ；可以获取设备名
import psutil #跨平台的进程管理和系统工具,用于系统资源的监控，分析，以及对进程


def getPlatform():
    print "获取操作系统信息"
    print platform.platform() #操作系统的名称和版本号
    print platform.version() #操作系统的版本号
    print platform.architecture() #操作系统的位数
def getMac(): #ubuntu查看：sudo lshw -C network ；多个网卡只会返回随机一个
    print "获取mac地址"
    node = uuid.getnode() #48位整数返回硬件地址，多个返回随机一个
    print node
    print type(node)
    print hex(node)
    print uuid.UUID(int=node)
    print uuid.UUID(int=node).hex[-12:]
    print uuid.uuid1()#基于时间戳和mac地址
def getTime(): #获取系统运行时间
    print "获取系统运行时间"
    print time.time() #放回当前时间的时间戳
    print int(time.time()) #转成整数 #argument must be 9-item sequence, not float,int
    print str(int(time.time()))
    print time.localtime() #返回当地时间的时间元祖
    print time.localtime(time.time())
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) #转化成时间字符串 参数为时间元祖
def getHostName():#获取主机名 ；查看：hostname 或 终端界面@
    print "获取主机名"
    print socket.gethostname()  #计算机的主机名
    print socket.getfqdn(socket.gethostname())
def getMem(): #查看：sudo dmidecode|grep -P -A5 "Memory Device" |grep Size 或 top / free
    print "获取内存"
    mem = psutil.virtual_memory()
    print psutil.virtual_memory()
    print mem.total / 1024.0 /1024.0 /1024.0 #单位为B,K,M,G
    print mem.percent
def getCpu():
    print "获取CPU的占用度"
    print psutil.cpu_percent()
    print psutil.cpu_percent(interval=1) #interval:时间间隔/秒


if __name__ == '__main__':
    getPlatform()
    getMac()
    getTime()
    getHostName()
    getMem()
    getCpu()