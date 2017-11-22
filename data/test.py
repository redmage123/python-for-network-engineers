#!/usr/bin/env python3

import xml.sax

class LibVirtHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.network = ''
        self.bridge = ''
        self.domain = ''
        self.ipv6 = ''

   def startElement(self,tag,attributes):
       if tag == 'Network':
           if 'ipv6' in attributes:
               self.ipv6 = True
           else:
               self.ipv6 = False
       elsif 


parser = xml.sax.make_parser()
parser.setContentHandler(LibvVirtHandler)
parser.parse(open('libvirt.xml','r'))


