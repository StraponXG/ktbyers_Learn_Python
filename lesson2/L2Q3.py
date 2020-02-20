from pprint import pprint

#create a list called show_arp, where all lines in file are items in list
with open("show_arp.txt") as file:
    show_arp = file.readlines()

#remove the first line
show_arp = show_arp[1:-1]

#pretty print
pprint(show_arp)
print("\n\n")

#sort
show_arp.sort()
pprint(show_arp)
print("\n\n")

#just the first three
top_three_arp_entries = show_arp[0:3]
pprint(top_three_arp_entries)
print("\n\n")

#create single string from first three entries
single_string_for_first_three_entries = "\n".join(top_three_arp_entries)
print(single_string_for_first_three_entries)

#output the single string of three lines to a file
with open("arp_entries.txt","wt") as output_file:
    output_file.write(single_string_for_first_three_entries)
