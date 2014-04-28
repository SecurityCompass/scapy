#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scapy.all import *
from scapy.utils import *

from espeak import espeak

load_contrib('http')
a=1
def f(p):
 l=p.lastlayer()
 if isinstance(l,Raw) or 'Option' in l.name:
  l=l.underlayer
 espeak.synth(l.name)
 return

if a:
 sniff(
iface='wlan0',lfilter=lambda p:not espeak.is_playing(),prn=f)
else:
 sniff(offline="a.cap",lfilter=lambda p:not espeak.is_playing(),prn=f)
