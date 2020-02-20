show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

show_version_trimmed = show_version.strip()
print(show_version_trimmed)

show_version_split = show_version_trimmed.split()
print(show_version_split)

model = show_version_split[1]
serial = show_version_split[2]

if "cisco" in model.lower():
    print("Vendor is Cisco")
else:
    print("Vendor is not Cisco")
    
if "881" in model.lower():
    print("Type is 881")
else:
    print("Type is not 881")

print("Model: %s \t Serial: %s" % (model, serial))