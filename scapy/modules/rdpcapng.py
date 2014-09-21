#!/usr/bin/env python
# encoding: utf-8

try:
    import pcap
except ImportError as e:
    import pcapy as pcap

import os

TEMP_DIR="/tmp"

@conf.commands.register
def rdpcapng(filename):
    tempf=TEMP_DIR+"/"+str(hash(filename))+".cap"
    pc = pcap.pcapObject()
    pc.open_offline(filename)
    pc.dump_open(tempf)
    pc.loop(0,None)
    sniffed = rdpcap(tempf)
    os.remove(tempf)
    sniffed.listname=filename
    return sniffed
