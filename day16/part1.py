from utils import *

with open("input.txt", "r") as input_file:
    lines = [e.replace("\n", "") for e in input_file.readlines()]



hex_code = lines[0]
# hex_code = "A0016C880162017C3686B18A3D4780"
bin_code = hex_to_bin(hex_code)

version = bin_to_dec(bin_code[0:3])
type_ID = bin_to_dec(bin_code[3:6])





if type_ID != 4:

    length_type = bin_to_dec(bin_code[6])
    packet = {
        "version": version,
        "type_ID": type_ID,
        "length_type": length_type,
        "bin_code": bin_code[7:]
    }

    processed_packet, _ = process_packet_operation(packet)

    print_packet(processed_packet)
    print(sum_versions(processed_packet))
