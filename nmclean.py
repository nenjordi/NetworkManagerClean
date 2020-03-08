import NetworkManager
import re
import os

# pattern = "br-.*"
pattern = "docker?.*"

c = NetworkManager.const


conns = dict()
activeconns = dict()
print("Connections")
for conn in NetworkManager.Settings.ListConnections():
    settings = conn.GetSettings()
    # print(str(conn) + " " + str(settings['connection']))
    #print(str(conn) + " " + str(settings['connection']['id']))
    if re.match(pattern, settings['connection']['id']):
        if settings['connection']['id'] not in conns.keys():
            conns[settings['connection']['id']] = list()
        conns[settings['connection']['id']].append(settings['connection']['uuid'])

print(str(conns))

print("Active Connections")
for conn in NetworkManager.NetworkManager.ActiveConnections:
    settings = conn.Connection.GetSettings()
    #print(str(conn) + " " + str(settings['connection']['id']))
    activeconns[settings['connection']['id']] = settings['connection']['uuid']
print(str(activeconns))


for c in conns.keys():
    for uuid in conns[c]:
        if uuid not in activeconns.values():
            print("Removing: " + uuid + " as " + c)
            os.system("nmcli c delete uuid " + uuid)
        else:
            print("NOT Removing: " + uuid + " from " + c)

