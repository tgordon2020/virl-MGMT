# utils functions



def devicelist(topology):
    import os
    from collections import defaultdict
    devices = defaultdict(list)
    for x in os.listdir(topology):
        for y in os.listdir(f"{topology}/{x}"):
            if "config" in y:
                y = y.split("-")[0]
                devices[x].append(y)
            else:
                pass
    return devices

def deviceip(device):
    devices = {"R1": "172.16.0.11",
               "R2": "172.16.0.12",
               "R3": "172.16.0.13",
               "R4": "172.16.0.14",
               "R5": "172.16.0.15",
               "R6": "172.16.0.16",
               "R7": "172.16.0.17",
               "R8": "172.16.0.18",
               "R9": "172.16.0.19",
               "R10": "172.16.0.20",
               "SW1": "172.16.0.21",
               "SW2": "172.16.0.22",
               "SW3": "172.16.0.23",
               "SW4": "172.16.0.24"}
    return(devices[device])
