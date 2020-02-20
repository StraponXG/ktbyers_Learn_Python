#initial list
ip_addresses = ["10.192.2.1","10.194.23.177","172.12.1.1","192.168.76.1","1.1.1.1"]
print(ip_addresses)

#append method
ip_addresses.append("10.1.1.1")
print(ip_addresses)

#extend method
extend_addresses = ["10.2.2.2","10.3.3.3"]
ip_addresses.extend(extend_addresses)
print(ip_addresses)

#concatenation method
concat_addresses = ["10.4.4.4","10.5.5.5"]
ip_addresses = ip_addresses + concat_addresses
print(ip_addresses)
concat_addresses

#print out differet sets
print(ip_addresses)
print(ip_addresses[0])
print(ip_addresses[-1])

#pop method
ip_addresses.pop(0)
ip_addresses.pop(-1)
print(ip_addresses)

#update first ip, then print it out
ip_addresses[0] = "99.99.99.99"
print(ip_addresses[0])