import json

with open("sample-data.json", "r") as json_file:
    data = json.load(json_file)
    
print("Interface Status")
print("=" * 85)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 85)

imdata = data["imdata"]

for item in imdata:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "") 
    speed = attributes.get("speed", "inherit")  
    mtu = attributes["mtu"]

    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<6}")