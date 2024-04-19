# # You have json containing meta information about a game build.

# # Create update() function that takes following arguments:
# # * initial_meta - initial meta information to modify
# # * command - append or delete
# # * namespace - namespace of value that needs to be appended or deleted
# # * value/s - value or list of values
# # * type - optional argument for append command, default is "1"

# # 1) Load json to python as "meta" variable
# # 2) Run update() with args (meta, "append", "GTL::Build::Tags", ["DX13", "Uplay", "DLSS"], 1)
# # 3) Run update() with arguments (meta_new, "delete", "GTL::Build::Categories", "NODRM")
# # 4) Output new meta info to json

# # All values of a namespace must be unique
# # Number order shouldn't have gaps f.e. 1, 3, 4 is wrong
# # Number order in the input/output array can be random f.e 4,2,3,1

# import json
# def update(initial_meta, command, namespace, values, type = 1) :
#     meta  =  initial_meta if initial_meta else []
#     if command == "append":
#         for value in values:
#             found  =  False
#             for item in meta:
#                 if item["Name"] == namespace and item["Type"] == type and item["Value"] == value:
#                     found = True
#                     break
#                 if not found:
#                     meta.append({
#                         "Name" : namespace,
#                         "Type" : type,
#                         "Value" : value
#                     })
#         # meta = sorted(meta, key = lambda x: int(x['Name'].split("::")[-1]))
#         meta = sorted(meta, key=lambda x: int(x['Name'].split("::")[-1]))

#     elif command == "delete":
#         for value in values:
#             for i, item in enumerate(meta):
#                 if item["Name"] == namespace and item["Type"] == type and item["Value"] == value:
#                     del meta[i]
#                     break
#     return meta

# meta = json.loads('''
# [
#     {
#         "Name": "GTL::Build::Tags::1",
#         "Type": 1,
#         "Value": "Aftermath"
#     },
#     {
#         "Name": "GTL::Build::Tags::2",
#         "Type": 1,
#         "Value": "SL"
#     },
#     {
#         "Name": "GTL::Build::Tags::3",
#         "Type": 1,
#         "Value": "NVNGX"
#     },
#     {
#         "Name": "GTL::Build::Tags::4",
#         "Type": 1,
#         "Value": "Steam"
#     },
#     {
#         "Name": "GTL::Build::Tags::5",
#         "Type": 1,
#         "Value": "DLSS"
#     },
#     {
#         "Name": "GTL::Build::Categories::1",
#         "Type": 1,
#         "Value": "NODRM"
#     },
#     {
#         "Name": "GTL::Build::Categories::2",
#         "Type": 1,
#         "Value": "GPDS"
#     }
# ]
# ''')

# with open("meta.json", "r") as f:
#     meta = json.load(f)

# meta_new = update(meta, "append", "GTL::Build::Tags", ["DX13", "Uplay", "DLSS"],1)

# meta_new = update(meta_new, "delete", "GTL::Build::Categories", "NODRM")

# with open("meta_updated.json", "w") as f:
#     json.dump(meta_new, f, indent=4)
import json

def update(initial_meta, command, namespace, values, type=1):
    meta = initial_meta if initial_meta else []
    
    if command == "append":
        for value in values:
            found = False
            for item in meta:
                if item["Name"] == namespace and item["Type"] == type and item["Value"] == value:
                    found = True
                    break
            if not found:
                meta.append({
                    "Name": namespace + "::" + str(len(meta) + 1),
                    "Type": type,
                    "Value": value
                })
    
    elif command == "delete":
        meta = [item for item in meta if not (item["Name"] == namespace and item["Type"] == type and item["Value"] in values)]
    
    return meta

meta = json.loads('''
[
    {
        "Name": "GTL::Build::Tags::1",
        "Type": 1,
        "Value": "Aftermath"
    },
    {
        "Name": "GTL::Build::Tags::2",
        "Type": 1,
        "Value": "SL"
    },
    {
        "Name": "GTL::Build::Tags::3",
        "Type": 1,
        "Value": "NVNGX"
    },
    {
        "Name": "GTL::Build::Tags::4",
        "Type": 1,
        "Value": "Steam"
    },
    {
        "Name": "GTL::Build::Tags::5",
        "Type": 1,
        "Value": "DLSS"
    },
    {
        "Name": "GTL::Build::Categories::1",
        "Type": 1,
        "Value": "NODRM"
    },
    {
        "Name": "GTL::Build::Categories::2",
        "Type": 1,
        "Value": "GPDS"
    }
]
''')

meta_new = update(meta, "append", "GTL::Build::Tags", ["DX13", "Uplay", "DLSS"], 1)
meta_new = update(meta_new, "delete", "GTL::Build::Categories", ["NODRM"])

with open("meta_updated.json", "w") as f:
    json.dump(meta_new, f, indent=4)
