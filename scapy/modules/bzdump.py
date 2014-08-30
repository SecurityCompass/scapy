#!/usr/bin/env python
# encoding: utf-8

import sys
import os

try:
    import Image# install PIL
except ImportError:
    from PIL import Image# install PIL

from scapy.plist import PacketList

palette8bit = [ b | (g<<8) | (r<<16) for b in range(0x0, 0x100, 0x33) for g in range(0x0, 0x100, 0x33) for r in range(0x0, 0x100, 0x33)] + [gr for gr in range(0x0, 0x1000000, 0x111111)] + [0xC0C0C0,0x808080,0x800000,0x800080,0x008000,0x008080]  + [0x000000 for i in range(17)] + [0xFFFFFF]
palette_array8bit = []
for idx,rgb in enumerate(palette8bit):
    s_rgb = "%06x" % rgb
    r = int(s_rgb[:2],16)
    g = int(s_rgb[2:4],16)
    b = int(s_rgb[4:],16)
    palette_array8bit.extend( (r, g, b) )

def _bzdump_list(self, x=256, lfilter=None,split=False):
    """
    Same as nsummary(), except that packets are also bzdumped
    lfilter: a function that decides whether a packet must be displayed
    """
    s = ""
    for i in range(len(self.res)):
        p = self._elt2pkt(self.res[i])
        if lfilter is not None and not lfilter(p):
            continue
        p_s = str(p)
        s += p_s
        if split:
            if len(p_s) % x:
                s += x*"\x05"# RED LINE
            else:
                s += (len(p_s) % x)*"\x00" # append new BLACK line
                s += x*"\x05"# RED LINE
    bzdump(s)

PacketList.bzdump = _bzdump_list

@conf.commands.register
def bzdump(s, x=256):
    """Draw psudo bitmap to xterm-256color"""
    s_size = len(s)
    y = s_size / x
    if s_size % x:
        y += 1
    img = Image.new('P', (x, y))
    img.putdata(s)
    img.putpalette(palette_array8bit)
    img.show()

if __name__ == "__main__":
    from scapy.main import interact
    from scapy.all import sniff
    my=sniff(prn=bzdump)
    interact(mydict=locals(),mybanner="***SYA-KE scapy!***")
