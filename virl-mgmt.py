import os
from utils import deviceip


# update gig0/0 configuration for OOBM
def gig00(ip):
    for i,v in enumerate(device_config):
        if "interface GigabitEthernet0/1\n" in v:
            gig00_index = i-1
        else:
            pass
    
    gig = ("!\n",
        "interface GigabitEthernet0/0\n"
        " description MGMT\n",
        " no switchport\n",
        " vrf forwarding MGMT\n",
        f" ip address {ip} 255.255.255.0\n",
        " duplex auto\n",
        " speed auto\n",)

    for y in reversed(gig):
        device_config.insert(gig00_index,y)


# insert VRF def in config
def hostname():
    for i,v in enumerate(device_config):
        if "hostname" in v:
            hostname_index = i+1
        else:
            pass
    device_config.insert(hostname_index,"!\nvrf definition MGMT\n !\n address-family ipv4\n exit-address-family\n!\n")

# insert http client device and VRF default route
def httpclient():
    for i,v in enumerate(device_config):
        if "line con 0" in v:
            linecon0_index = i-1
        else:
            pass
    device_config.insert(linecon0_index,"!\nip http client source-interface GigabitEthernet0/0\nip route vrf MGMT 0.0.0.0 0.0.0.0 172.16.0.1\nno cdp log mismatch duplex\n")

# insert VTY config for mgmt
def vty04():
    for i,v in enumerate(device_config):
        if "vty" in v:
            vty_index = i + 1
        elif "end\n" in v:
            end_index = i

    for x in range(vty_index,end_index):
        device_config.pop(vty_index)

    vty_config = (" privilege level 15\n",
                  " password password\n",
                  " login\n",
                  " transport input all\n",
                  "!\n")

    for y in reversed(vty_config):
        device_config.insert(vty_index,y)

for x in os.listdir("topologies"):
    for y in os.listdir(f"topologies/{x}"):
        if "config" in y:
            device_ip = deviceip(y.split("-")[0])
            with open(f"topologies/{x}/{y}", "r") as config:
                device_config = config.readlines()
            if "interface GigabitEthernet0/0\n" in device_config:
                pass
            else:
                try:
                    gig00(device_ip)
                except:
                    print(f"issues adding gig0/0 mgmt interface in topologies/{x}/{y}, manually edit file") 

            if "vrf definition MGMT\n" in device_config:
                pass
            else:
                try:
                    hostname()
                except:
                    print(f"issues adding MGMT vrf to to toplogies/{x}/{y}, manually edit file")
    
            if " password password\n" in device_config:
                pass
            else:
                try:
                    vty04()
                except:
                    print(f"issues adding VTY 0 4 config to topologies/{x}/{y}")

            if "ip http client source-interface GigabitEthernet0/0\n" in device_config:
                pass
            else:
                try:
                    httpclient()
                except:
                    print(f"issues adding http client and VRF route to topologies/{x}/{y}")

            with open(f"topologies/{x}/{y}", "w") as config_update:
                config_update.writelines(device_config)
