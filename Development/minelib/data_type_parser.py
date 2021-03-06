"""
SOURCE: This file is taken from a Google Code project called py-mine-client,
which is outdated now. This file still worked so I wanted to make use of it.

This file does the conversion between Java(actually C) data types and their 
Python equivalents. It uses struct to do this.

"""

from struct import pack, unpack

def char(data):
    return pack('>c', data)

def parse_char(sio):
    return unpack('>c', sio.read(1))[0]

def byte(data):
    return pack('>b', data)

def parse_byte(sio):
    return unpack('>b', sio.read(1))[0]

def short(data):
    return pack('>h', data)

def parse_short(sio):
    return unpack('>h', sio.read(2))[0]

def shortchar(data):
    return pack('>H', ord(data))

def parse_shortchar(sio):
    return chr(unpack('>H', sio.read(2))[0])

def int(data):
    return pack('>i', data)

def parse_int(sio):
    return unpack('>i', sio.read(4))[0]

def long(data):
    return pack('>q', data)

def parse_long(sio):
    return unpack('>q', sio.read(8))[0]

def float(data):
    return pack('>f', data)

def parse_float(sio):
    return unpack('>f', sio.read(4))[0]

def double(data):
    return pack('>d', data)

def parse_double(sio):
    return unpack('>d', sio.read(8))[0]

def string8(data):
    return short(len(data)) + data

def parse_string8(sio):
    length = parse_short(sio)
    return sio.read(length)

def string16(data):
    chars = ''.join([shortchar(i) for i in data])
    return short(len(data)) + chars

def parse_string16(sio):
    length = parse_short(sio)
    result = ''
    for i in range(length):
        result += parse_shortchar(sio)
    return result

def bool(data):
    if data:
        return '\x01'
    else:
        return '\x00'

def parse_bool(sio):
    data = sio.read(1)
    if data == '\x01':
        return True
    else:
        return False
