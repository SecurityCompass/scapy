## This file is part of Scapy
## See http://www.secdev.org/projects/scapy for more informations
## Copyright (C) Philippe Biondi <phil@secdev.org>
## This program is published under a GPLv2 license

from scapy.packet import Packet,bind_layers
from scapy.fields import Field,ByteField,XByteField,IntField
from scapy.layers.l2 import EAP

class ThreeBytesField(ByteField):
    def __init__(self, name, default):
        Field.__init__(self, name, default, "!I")
        self.sz = 3
    def addfield(self, pkt, s, val):
        return s+struct.pack(self.fmt, self.i2m(pkt,val))[1:4]
    def getfield(self, pkt, s):
        return  s[3:], self.m2i(pkt, struct.unpack(self.fmt, "\x00"+s[:3])[0])

class XThreeBytesField(ThreeBytesField,XByteField):
    def i2repr(self, pkt, x):
        return XByteField.i2repr(self, pkt, x)

class EAP_Expanded(Packet): # eap type 254
    name = "Expanded EAP"
    fields_desc = [ XThreeBytesField("vendor_id", 0),
                    IntField("vendor_type", 0)
                ]

bind_layers( EAP, EAP_Expanded, type=254)
