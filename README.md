scapy
=====
Scapyは小規模のパケットを解析・構築するためのツールです。  
このリポジトリは、Scapyの公式リポジトリ<http://bb.secdev.org/scapy>から  
最新のものを持ってきて、sya-keが個人的に修正したり、  
つけてみたい機能を勝手に追加したものです。常に最新のものをpullしてきています。

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
$ sudo find /usr/local/share/ -name "scapy*" | xargs rm
```

License
=====
GPL version 2 (See "LICENSE")

Author
=====
ppl in <http://bb.secdev.org/scapy>
