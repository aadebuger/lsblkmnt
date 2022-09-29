import os
import json
diskv = filter(lambda item: item['mountpoint'] is None and item['uuid'] is not None ,data['blockdevices'])

#lsblk -o PATH,SIZE,MOUNTPOINT,UUID,MODEL -J
for disk in list(diskv):
    mntname="/mnt/hdd{}".format(chr(ord('a')+disknum))
    disknum  = disknum + 1
    print("UUID={0} {1} ext4 defaults 	0 	0".format(disk['uuid'],mntname))

disknum = 0

for disk in list(diskv):
    mntname="/mnt/hdd{}".format(chr(ord('a')+disknum))
    disknum  = disknum + 1
    print("mkdir {1}".format(disk['uuid'],mntname))

f = open('diskm.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
 
# Closing file
f.close()
print(data)
print(data['blockdevices'])
for disk in data['blockdevices']:
    print(disk)

diskv = filter(lambda item: item['mountpoint'] is not None and  item['mountpoint'].startswith("/mnt") and item['uuid'] is not None ,data['blockdevices'])

def checkPlot(files):
        for file in files:
            if file.endswith("plot"):
                return True
        return False
def findPlotdir(mntdir):
    plotdir=[]
    for root, dirs, files in os.walk(mntdir):
        print(root)
        print(files)
        if checkPlot(files):
            print("find plot",root)
            plotdir.append(root)
    return plotdir

plotdirv=map(lambda item:findPlotdir(item['mountpoint']),diskv)

plotv=[]
for plot in plotdirv:
    print(plot)
    for item in plot:
        plotv.append(item)

import io
import yaml
with open("/home/aadebuger/linux/config.yaml", 'r') as stream:
    data_loaded = yaml.safe_load(stream)

data_loaded['path']=plotv

with io.open('myconfig.yaml', 'w', encoding='utf8') as outfile:
    yaml.dump(data_loaded, outfile, default_flow_style=False, allow_unicode=True)
