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

from scapy.contrib.extra.eap.expanded import EAP_Expanded

#http://www.vocal.com/secure-communication/eap-types/
eap_types = {
0:'Reserved',
1:'Identify',
2:'Notification',
3:'Legacy NAK (Response Only)',
4:'MD5-Challenge',
5:'OTP, One Time Password',
6:'GTC, Generic Token Card',
9:'RSA Public Key Authentication',
10:'RSA Public Key Authentication',
11:'KEA',
12:'KEA-VALIDATE',
13:'EAP-TLS Authentication Protocol',
15:'RSA Security SecurID EAP',
18:'EAP-SIM, GSM Subscriber Identity Modules',
19:'SRP-SHA-1 Part 1',
20:'SRP-SHA-1 Part 2',
21:'EAP-TTLS, EAP Tunneled TLS Authentication Protocol',
23:'EAP-AKA, EAP method for 3rd Generation Authentication and Key Agreement',
25:'PEAP, Protected EAP',
26:'MS-EAP-Authentication (EAP/MS-CHAPv2)',
27:'EAP-MAKE, Mutual Authentication w/Key Exchange',
29:'PEAPv0/EAP-MSCHAPv2',
32:'EAP-POTP, Protected One Time Password',
33:'MS-Authentication-TLV',
43:'EAP-FAST, EAP Flexible Authentication via Secure Tunneling',
46:'EAP-PAX, EAP Password Authentication eXchange',
47:'EAP-PSK, EAP Pre-Shared Authentication and Key Establishment',
48:'EAP-SAKE, EAP Shared-secret Authentication and Key Establishment',
49:'EAP-IKEv2',
50:'EAP-AKA, Improved EAP method for 3rd Generation Authentication and Key Agreement',
51:'EAP-GPSK, EAP Generalized Pre-Shared Key',
254:'Expanded Type',
255:'Experimental',
}

__all__ = ["PEAP","LEAP","EAP_TTLS","EAP_TLS","EAP_Fast","EAP_Expanded"]
