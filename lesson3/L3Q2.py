from pprint import pprint

#create a list called show_vlan, where all lines in file are items in list
with open("lesson3/show_arp.txt") as file:
    show_arp = file.readlines()

#pprint(show_arp)
found_gateway = False
found_arista = False

#go through each line in the show_arp list
for line in show_arp[:]:
    split_line = line.split()
    ip_address = split_line[1]
    mac_address = split_line[3]

    if "10.220.88.1" in split_line:
        print("{:<25}{:^16}{:^17}".format("Default gateway IP/MAC:",ip_address, mac_address))
        found_gateway = True
    elif "10.220.88.30" in split_line:
        print("{:<25}{:^16}{:^17}".format("Arista3 IP/Mac is:",ip_address, mac_address))
        found_arista = True
    
    if found_gateway and found_arista:
        break



