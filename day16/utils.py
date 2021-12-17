from utils_main import hex_to_bin, bin_to_dec


def process_packet_operation(packet_to_process):
    bin_code = packet_to_process["bin_code"]
    length_type = packet_to_process["length_type"]


    processed_packet = {
        "version": packet_to_process["version"],
        "type_ID": packet_to_process["type_ID"],
        "packets": []
    }
    if length_type == 0:
        length = bin_to_dec(bin_code[0:15])
        bin_code = bin_code[15:]




        while length:
            old_len = len(bin_code)
            packet = {
                "version": bin_to_dec(bin_code[0:3]),
                "type_ID": bin_to_dec(bin_code[3:6]),
            }
            bin_code = bin_code[6:]

            if packet["type_ID"] == 4:
                loop = 1
                word = ""
                while loop:
                    loop = bin_to_dec(bin_code[0])
                    word += bin_code[1:5]
                    bin_code = bin_code[5:]
                length -= (old_len - len(bin_code))
                packet["value"] = bin_to_dec(word)
            else:
                packet["length_type"] = bin_to_dec(bin_code[0])
                packet["bin_code"] = bin_code[1:]
                packet, bin_code = process_packet_operation(packet)
                length -= (old_len - len(bin_code))
            processed_packet["packets"].append(packet)

        return processed_packet, bin_code
    elif length_type == 1:
        num_packets = bin_to_dec(bin_code[0:11])
        bin_code = bin_code[11:]

        for i in range(num_packets):
            packet = {
                "version": bin_to_dec(bin_code[0:3]),
                "type_ID": bin_to_dec(bin_code[3:6]),
            }
            bin_code = bin_code[6:]
            if packet["type_ID"] == 4:
                loop = 1
                word = ""
                while loop:
                    loop = bin_to_dec(bin_code[0])
                    word += bin_code[1:5]
                    bin_code = bin_code[5:]
                packet["value"] = bin_to_dec(word)
            else:
                packet["length_type"] = bin_to_dec(bin_code[0])
                bin_code = bin_code[1:]
                packet["bin_code"] = bin_code
                packet, bin_code = process_packet_operation(packet)
            processed_packet["packets"].append(packet)
        return processed_packet, bin_code


def print_packet(packet, level=0):
    print("\t" * level + f"'version': {packet['version']}")
    print("\t" * level + f"'type_ID': {packet['type_ID']}")

    if 'value' in packet.keys():
        print("\t" * level + f"'value':{packet['value']}\n")
    else:
        for sub_packet in packet['packets']:
            print_packet(sub_packet, level + 1)


def sum_versions(packet):
    res = int(packet["version"])

    if 'packets' in packet.keys():
        for sub_packet in packet['packets']:
            res += sum_versions(sub_packet)

    return res