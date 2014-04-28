# -*- coding: utf-8 -*-
## This file is part of Scapy
## See http://www.secdev.org/projects/scapy for more informations
## Copyright (C) Philippe Biondi <phil@secdev.org>
## This program is published under a GPLv2 license

from scapy.packet import *
from scapy.fields import *
from scapy.layers.inet import UDP
from re import search

class StrStopFieldStripped(StrStopField):
  
    def i2h(self, pkt, x):
	return x.rstrip()
        

class FieldListStr(FieldListField):

    def __init__(self, name, default, field, length_from=None, count_from=None, length_terminator=None):
        if default is None:
            default = []  # Create a new list for each instance
        Field.__init__(self, name, default)
        self.count_from = count_from
        self.length_from = length_from
        self.field = field
        self.length_terminator = length_terminator

    def getfield(self, pkt, s):
	
	#print 'LUNGHEZZA field attuale contiene terminatore?: ',  self.field.getfield(pkt,s)[0][:self.field.getfield(pkt,s)[0].find('\r\n\r\n')]

	c = l = None
	if self.length_from is not None:
	    l = self.length_from(pkt)
	elif self.count_from is not None:
	    c = self.count_from(pkt)
	elif self.length_terminator is not None:
	    l = s.find(self.length_terminator)+len(self.length_terminator)
	     
	val = []
	ret=""
	if l is not None:
	    s,ret = s[:l],s[l:]
	    
	while s:
	    if c is not None:
		if c <= 0:
		    break
		c -= 1
	    s,v = self.field.getfield(pkt, s)
	    val.append(v)
	return s+ret, val
        
        
    def i2h(self, pkt, x):
	if type(x) is list:
            return [v.strip() for v in x]
	return x.rstrip()
      

class SIP(Packet):
    name="SIP"
    fields_desc = [ StrStopFieldStripped("FirstCommand",""," ") ]
    
    def guess_payload_class(self, payload):
	
	if self.FirstCommand in ['REGISTER', 'INVITE', 'ACK', 'CANCEL', 'BYE', 'OPTIONS'] :
            return SIP_REQUEST
        elif self.FirstCommand[:4]  == 'SIP/':
            return SIP_STATUS
        else:
	    return NoPayload()
	    #return Packet.guess_payload_class(self, payload)
    
class SIP_REQUEST(Packet):
    name="SIP request"
    fields_desc = [ StrStopFieldStripped("RequestUri",""," "), StrStopFieldStripped("SIPVersion","","\r\n") ]
    
class SIP_STATUS(Packet):
    name="SIP status"
    fields_desc = [ StrStopFieldStripped("StatusCode",""," "), StrStopFieldStripped("ReasonPhrase","","\r\n") ]

class SIP_HEADER(Packet):
    name="SIP header"
    fields_desc = [ FieldListStr("Header", [] ,StrStopFieldStripped("parameters","", "\r\n"), length_terminator='\r\n\r\n') ]

class SDP(Packet):
    name="SDP"
    fields_desc = [ FieldListStr("SDP", [] ,StrStopFieldStripped("parameters","", "\r\n")) ]
    
    
bind_layers( UDP,           SIP,     dport=5060)
bind_layers( UDP,           SIP,     sport=5060)
bind_layers( UDP,           SIP,     dport=5061)
bind_layers( UDP,           SIP,     sport=5061)

bind_layers( SIP_REQUEST,           SIP_HEADER, )
bind_layers( SIP_STATUS,           SIP_HEADER, )

bind_layers( SIP_HEADER,           SDP, )