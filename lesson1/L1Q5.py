mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac1Split = mac1.split()
mac2Split = mac2.split()
mac3Split = mac3.split()

print(mac1Split)

ipAddr = {}
ipAddr["ip1"] = mac1Split[1]
ipAddr["mac1"] = mac1Split[3]

ipAddr["ip2"] = mac2Split[1]
ipAddr["mac2"] = mac2Split[3]

ipAddr["ip3"] = mac3Split[1]
ipAddr["mac3"] = mac3Split[3]

print(ipAddr)

#display everything in a fancy looking table
print()
print("{:>20} {:>20}".format("IP ADDR", "MAC ADDRESS"))
print("{:>20} {:>20}".format("-"*19, "-"*19))
print("{:>20} {:>20}".format(ipAddr['ip1'], ipAddr['mac1']))
print("{:>20} {:>20}".format(ipAddr['ip2'], ipAddr['mac2']))
print("{:>20} {:>20}".format(ipAddr['ip3'], ipAddr['mac3']))
print()