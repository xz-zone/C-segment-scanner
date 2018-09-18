##0x00 前言
很多时候在渗透一个比较大的目标时候，在前期信息收集过程中，我们会发现目标出口规模特别大，有一个或者多个C段甚至B段甚至更大。为了方便撕开口子，所以我们经常需要对目标出口段进行扫描。之前使用的中间件扫描器误报率太高，所以重构了下代码，实现利用网站转换IP，在进行C段端口收集。
##0x01 扫描运用到的模块
1.安装python3.7工具。

python官方网站：https://www.python.org

2.安装nmap工具

2.1首先yum下载安装一个nmap

`yum -y install nmap`

2.2在安装python3的模块,这里python3是我自定义的一个变量，可以在环境下自行设置

`python3 -m pip install nmap`

3.模块源码安装

3.1远程下载nmap模块

`wget http://xael.org/pages/python-nmap-0.6.1.tar.gz`

3.2解压nmap模块

`tar -zxvf python-nmap-0.6.1.tar.gz`

3.3进入nmap模块

`cd python-nmap-0.6.1`

3.4安装nmap模块

`python3 setup.py install`

4.安装运用到模块

4.1安装socket模块

`python3 -m pip install socket`

4.2安装命令行解析接口

`python3 -m pip install optparse`

4.3安装多线程模块

`python3 -m pip install threading`