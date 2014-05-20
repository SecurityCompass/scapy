#!/usr/bin/env python
# encoding: utf-8

@conf.commands.register
def tcpdump():
    conf.color_theme = scapy.themes.DefaultTheme()
    return sniff(prn=repr)
