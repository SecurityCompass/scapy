#!/usr/bin/env python
# encoding: utf-8

__author__ = "SYA-KE <syakesaba@gmail.com>"

# load me using load_module
# load_module("serialize")

import json
from scapy.all import *# for globals()

def jsondump(p,filename=None):
    """dump packet as json.

    @param p: Packet or PacketList
    @param filename: filename to dump to (if None, dump to str)
    @type command: str
    """
    return dump_packet_as_json(p, filename)

def dump_packet_as_json(p,filename=None):
    s = _dump_packet_as_str(p)
    if filename is not None:
        json.dump(s, file(filename,"wb"),ensure_ascii=False)
        return
    else:
        return s

def _dump_packet_as_str(p):
    if isinstance(p, PacketList):
        return [_dumps_json(pkt) for pkt in p]
    elif isinstance(p, Packet):
        return [_dumps_json(p),]
    else:
        raise TypeError("Packet or PacketList allowed for argument 1")

def _dumps_json(p):
    i = 0
    serialized = []
    if type(p) == tuple:#for traceroute packetlist
        p = p[0]
    layer = p.getlayer(i)
    while layer:
        serialized.append((layer.__class__.__name__,layer.fields))
        i += 1
        layer = p.getlayer(i)
    return serialized

@conf.commands.register
def jsonload(filename):
    """ laod json file as PacketList

    @param filename: filename to load json PacketList
    @type filename: str
    """
    p = json.load(file(filename,"rb"))
    return PacketList(jsonloads(p),name=filename)

@conf.commands.register
def jsonloads(p):
    """ laod json string as PacketList

    @param p: string to load json PacketList
    @type p: str
    """
    if isinstance(p, Packet):
        return PacketList(_loads_json(p))
    if isinstance(p, list) or isinstance(p, tuple):
        return PacketList([_loads_json(pkt) for pkt in p])

def _loads_json(s):
    deserialized = None
    for i in range(len(s)):
        serialized = s[i]
        layer = globals().get(serialized[0] ,None)
        if layer is None:
            print "Could not read class ",serialized[0]
            continue
        layer = layer()
        layer.fields = serialized[1]
        if deserialized is None:
            deserialized = layer
        else:
            deserialized = deserialized / layer
    return deserialized

PacketList.jsondump = dump_packet_as_json
Packet.jsondump = dump_packet_as_json
