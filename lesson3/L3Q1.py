from pprint import pprint

#create a list called show_vlan, where all lines in file are items in list
with open("lesson3/show_vlan.txt") as file:
    show_vlan = file.readlines()

#pprint(show_vlan)

#create new list for all our vlan_id / vlan_name tuples
vlan_list = []

#go through each line in the show_vlan list
for line in show_vlan[:]:
    split_line = line.split()
    vlan_id = split_line[0]
    vlan_name = split_line[1]
    
    #check whether the vlan_id entry is a number, if it is then append it to the vlan_list, otherwise pass
    try:
        int(vlan_id)
    except:
        pass
    else:
        vlan_list.append((vlan_id,vlan_name)) #this needs to be double bracketed because the append method can only assign a single variable
                                              #the inner braces represents a single tuple rather than 2 separate variables

print(vlan_list)
