## This file is part of Scapy
## See http://www.secdev.org/projects/scapy for more informations
## Copyright (C) Philippe Biondi <phil@secdev.org>
## This program is published under a GPLv2 license

from scapy.packet import Packet,bind_layers
from scapy.fields import ByteField,FieldLenField,StrLenField,StrField
from scapy.layers.l2 import EAP

class LEAP(Packet): # eap type 17
    name = "LEAP"
    fields_desc = [ ByteField("version", 1),
                    ByteField("reserved", 0),
                    FieldLenField("length", None, length_of="data", fmt="B"),
                    StrLenField("data", "", length_from=lambda pkt:pkt.length),
                    StrField("name", "")
    ]

bind_layers( EAP, LEAP, type=17)
