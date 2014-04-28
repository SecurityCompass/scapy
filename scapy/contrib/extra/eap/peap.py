## This file is part of Scapy
## See http://www.secdev.org/projects/scapy for more informations
## Copyright (C) Philippe Biondi <phil@secdev.org>
## This program is published under a GPLv2 license

from scapy.packet import Packet,bind_layers
from scapy.fields import FlagsField,BitField,ConditionalField,IntField
from scapy.layers.l2 import EAP

from scapy.contrib.extra.ssl import TLSv1RecordLayer

class PEAP(Packet): # eap type 25
    name = "PEAP"
    fields_desc = [ FlagsField("flags", 0, 6, ['reserved3', 'reserved2', 'reserved1', 'start', 'fragmented', 'length']),
                    BitField("version", 0, 2),
                    ConditionalField(IntField("length", 0), lambda pkt:pkt.flags > 31),
                ]

    def guess_payload_class(self, payload):
        if self.flags > 31:
            return TLSv1RecordLayer
        else:
            return Packet.guess_payload_class(self, payload)

bind_layers( EAP, PEAP, type=25)
