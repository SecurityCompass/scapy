scapy
=====

clone of Scapy official repository http://hg.secdev.org/scapy  version=2.2.0

CangeLog
=====
最新のpython-visualでtrace3Dをできるようにした。  
バイトバッファーのパケットを読み込めるようにした。  
それに関して、scapyが勝手に裏でgzip展開しているのを無くした。  
bitmapdumpを追加。色は256フルで使っているが、間引きたいところ。

Install
=====
```sh
$ sudo python setup.py install
```

Uninstall
=====
```sh
$ sudo rm -f `which scapy`
$ sudo rm -f `which UTscapy`
$ scapy
Welcome to Scapy (2.2.0-dev)
>>> scapy
<module 'scapy' from '/usr/local/lib/python2.6/dist-packages/scapy/__init__.pyc'>
$ sudo rm -rf /usr/local/lib/python2.6/dist-packages/scapy*
```

