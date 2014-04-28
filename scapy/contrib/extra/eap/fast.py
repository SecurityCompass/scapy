## This file is part of Scapy
## See http://www.secdev.org/projects/scapy for more informations
## Copyright (C) Philippe Biondi <phil@secdev.org>
## This program is published under a GPLv2 license

from scapy.packet import Packet,bind_layers
from scapy.fields import FlagsField,BitField,ConditionalField,IntField
from scapy.layers.l2 import EAP

from scapy.contrib.extra.ssl import TLSv1RecordLayer

class EAP_Fast(Packet): # eap type 43
    name = "EAP-Fast"
    fields_desc = [ FlagsField("flags", 0, 5, ['reserved2', 'reserved1', 'start', 'fragmented', 'length']),
                    BitField("version", 0, 3),
                    ConditionalField(IntField("length", 0), lambda pkt:pkt.flags > 15),
    ]
    def guess_payload_class(self, payload):
        if self.flags > 15:
            return TLSv1RecordLayer
        else:
            return Packet.guess_payload_class(self, payload)

bind_layers( EAP, EAP_Fast, type=43)
