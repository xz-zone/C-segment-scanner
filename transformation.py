# coding:utf-8
import threading
import sys

import socket
import nmap

import time
import optparse
from queue import Queue

event = threading.Event()
event.set()
q = Queue(-1)

class multi_thread(threading.Thread):
    def __init__(self,num,q):
        threading.Thread.__init__(self)
        self.num = num
        self.q = q

    def run(self):
        while event.is_set():
            if self.q.empty():
                event.clear()
            else:
                ip = self.q.get()
                self.ip_port(ip)

    def ip_port(self, ip):
        host = self.www_ip(ip)
        if host:
            iplist = host.split('.')
            for i in range(1, 255):
                try:
                    ip = str(iplist[0])+str('.')+str(iplist[1])+str('.')+str(iplist[2])+str('.')+str(i);
                    if self.nmaps(ip, 80) or self.nmaps(ip, 443):
                        self.save(ip)
                    time.sleep(0.5)
                except Exception as e:
                    print(e)

    def www_ip(self, url):
        try:
            result = socket.getaddrinfo(url, None)
            return result[0][4][0]
        except:
            return False

    def nmaps(self,tgtHost,tgtPort):
        nmScan = nmap.PortScanner()
        try:
            result = nmScan.scan(tgtHost,str(tgtPort))
            state = result['scan'][tgtHost]['tcp']
            if state[int(tgtPort)]['state'] == 'open':
                return tgtHost
            else:
                return False
        except Exception as e:
            return False
            
    def save(self, ip):
        with open('successs.txt', 'at') as f:
            f.writelines(ip + '\n')

def scan_thread(thread_num):     #参数是队列
    threads = []
    for num in range(1,thread_num+1):
        t = multi_thread(num,q)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def get_ip(path):
    with open(path, 'rt') as f:
        for ip in f.readlines():
            q.put(ip.strip())

if __name__ == '__main__':
    parse=optparse.OptionParser(usage='"Usage:%prog --path <path> --thread <thread>"',version="1.0")
    parse.add_option('-p','--path',dest='path',type=str,help='Please enter the URL file address.')
    parse.add_option('-t','--thread',dest='thread',type=int,default=100,help='Please enter the thread number.')
    parse.add_option('-v',help='Domain name conversion IP scan C segment!!')
    options,args=parse.parse_args()
    if options.path == None or options.thread == None:
      txt = '''
        Chinese Preview：
          -p 请输入你要扫描的url文件
          -t 请输入你要扫描线程数
          -v 查看版本
        Overseas Preview：
          -p Please enter the URL file address.
          -t Please enter the thread number.
      '''
      print(txt)
      exit(0)
    else:
        get_ip(options.path)
        scan_thread(options.thread)