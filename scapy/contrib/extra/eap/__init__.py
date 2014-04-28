#!/usr/bin/env python
# encoding: utf-8

## This file is part of Scapy
## See http://www.secdev.org/projects/scapy for more informations
## Copyright (C) Philippe Biondi <phil@secdev.org>
## This program is published under a GPLv2 license

#load_contrib("eap")

from scapy.contrib.extra.eap.peap import PEAP
from scapy.contrib.extra.eap.leap import LEAP
from scapy.contrib.extra.eap.ttls import EAP_TTLS
from scapy.contrib.extra.eap.tls import EAP_TLS
from scapy.contrib.extra.eap.fast import EAP_Fast

eap_types = {
    1:"ID",
    2:"NOTIFICATION",
    3:"LEGACY NAK",
    4:"MD5",
    5:"ONE TIME PASSWORD",
    6:"GENERIC TOKEN CARD",
    13:"EAP-TLS",
    17:"LEAP",
    18:"EAP-SIM",
    21:"EAP-TTLS",
    23:"EAP-AKA"
    25:"PEAP",
    43:"EAP-FAST",
    254:"EXPANDED EAP",
}

__all__ = ["PEAP","LEAP","EAP_TTLS","EAP_TLS","EAP_Fast"]
