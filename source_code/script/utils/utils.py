import binascii
 
def crc32(data):
    return binascii.crc32(data) & 0xffffffff
 


if __name__=='__main__':
    # 测试CRC
    data = "Hello, World!"
    binary = bin(int.from_bytes(data.encode(), 'big'))[2:]
    # checksum = crc32(data)
    # print(f"CRC-32: {checksum:#010x}")