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
0:"Reserved",
1:"Identify",
2:"Notification",
3:"NAK",
4:"MD5-Challenge",
5:"OTP",
6:"GTC",
7:"Allocated",
8:"Allocated",
9:"RSA",
10:"RSA",
11:"KEA",
12:"KEA-VALIDATE",
13:"EAP-TLS",
14:"Quest Defender Token",
15:"RSA Security SecurID EAP",
16:"Arcot System EAP",
17:"Cisco-LEAP",
18:"EAP-SIM",
19:"SRP-SHA-1 Part 1",
20:"SRP-SHA-1 Part 2",
21:"EAP-TTLS",
22:"Remote Access Service",
23:"EAP-AKA",
24:"EAP-3Com Wireless",
25:"PEAP",
26:"MS-EAP-Authentication (EAP/MS-CHAPv2)",
27:"EAP-MAKE",
28:"CRYPTOCard",
29:"PEAPv0/EAP-MSCHAPv2",
30:"DynamID",
31:"Rob EAP",
32:"EAP-POTP, Protected One Time Password",
33:"MS-Authentication-TLV",
34:"SentriNET",
35:"EAP-Actiontec Wireless",
36:"Cogent Systems Biometrics Authentication EAP",
37:"AirFortress EAP",
38:"EAP-HTTP Digest",
39:"SecureSuite EAP",
40:"DeviceConnect EAP",
41:"EAP-SPEKE",
42:"EAP-MOBAC",
43:"EAP-FAST",
44:"ZLXEAP",
45:"EAP-Link",
46:"EAP-PAX",
47:"EAP-PSK",
48:"EAP-SAKE",
49:"EAP-IKEv2",
50:"EAP-AKA Improved",
51:"EAP-GPSKD",
}

eap_types.update( {i+52:"For Designated Expert" for i in range(192-52)} )
eap_types.update( {i+192:"Reserved for Standards" for i in range(253-192)} )
eap_types.update( {254:"Expanded TypeError"} )
eap_types.update( {255:"Experimental"} )

__all__ = ["PEAP","LEAP","EAP_TTLS","EAP_TLS","EAP_Fast","EAP_Expanded"]
