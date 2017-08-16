from win32wifi.Win32Wifi import getWirelessInterfaces
from win32wifi.Win32Wifi import getWirelessAvailableNetworkList

if __name__ == "__main__":
    ifaces = getWirelessInterfaces()
    for iface in ifaces:
        guid = iface.guid
        networks = getWirelessAvailableNetworkList(iface)
        for network in networks:
            print(network)
            print("-" * 20)

