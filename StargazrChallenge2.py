import os,random
path="./datasets/logs"
files=os.listdir(path)
names=[]
for file in files:
    names.append(file[:-4])

i=-1
i2=random.randint(0,len(names)-1)

# These computers only connect in local network when attacked, so we have to look for the
# first one to communicate in the local network
# Starting from a random computer in the network (i2) we jump between first IN connections
# until we always arrive to 172.16.41.255 which is the first one to communicate, thus this
# is the one to initiate the attack

while(i!=i2):
    i=i2
    print("\nFile: "+i.__str__()+" - Computer IP: "+names[i].__str__())
    f=open(path+"/"+files[i])
    lines=f.readlines()


    # for line in lines:
    j = 0
    found=False
    while(not found):

    # line=lines[0]
        line=lines[j].split(" ")
        if line[0]=="IN":
            if names.__contains__(line[1][:-1]):
                print("Contacted by: "+line[1][:-1].__str__())
                i2=names.index(line[1][:-1])
                found=True
        j+=1

print("\nAttack initiated by: "+names[i].__str__())
