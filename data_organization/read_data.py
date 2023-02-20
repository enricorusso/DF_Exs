import struct

# < little endian, H unsigned short (2 bytes), s string, c char (1 byte) 
fmt = "<H29sc"
struct_unpack = struct.Struct(fmt).unpack_from

length = struct.calcsize(fmt)
print(f"Size of data structure: {length} bytes")

with open("data_structure_flag.bin", "rb") as f:
    data = f.read(length)
    while data:
        res = struct_unpack(data)
        print(f"- house number: {res[0]}, street name: {res[1].decode()}")
        if res[2][0] & 0x01:
            city = f.read(16)
            print(f"  city: {city.decode()}")
        data = f.read(length)