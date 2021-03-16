from os import system
from subprocess import getoutput

def getShell():
    print("Enter q or quit to Exit this shell\n")
    while True:
        user = getoutput("whoami")
        host = getoutput("hostname")
        cmnd = str(input("\n[{}@{} ~] ".format(user, host)))
        if cmnd in ['q', 'quit']:
            break
        system(cmnd)

def listDisks():
    system("lsblk -a")

def fdiskutil():
    print("\nDISK LIST - \n")
    system("fdisk -l | grep /dev")
    print("\nFDISK UTILITY - \n")
    diskname = input("Enter Disk Name: ")
    print()
    system("fdisk {}".format(diskname))

def formatDisk():
    ft = input("Full or Resized Format (Enter F or R): ")
    if ft.lower() == 'f':
        print("\nDISK LIST - \n")
        system("lsblk -a")
        print("\nFORMAT FULL DISK - \n")
        diskname = input("Enter Disk Name: ")
        frmtType = input("Fromat Type: ")
        print()
        system("mkfs -t {} {}".format(frmtType, diskname))
    elif ft.lower() == 'r':
        print("\nDISK LIST - \n")
        system("lsblk -a")
        print("\nFORMAT RESIZED DISK - \n")
        diskname = input("Enter Disk Name: ")
        print()
        system("resize2fs {}".format(diskname))
    else:
        print("Enter F or R")
        formatDisk()

def mountUmountDisk():
    ft = input("Mount or Unmount Disk (Enter M or U): ")
    if ft.lower() == 'm':
        print("DISK LIST - \n")
        system("lsblk -a")
        print("\nMOUNT DISK - \n")
        diskname = input("Enter Disk Name: ")
        mntPath = input("Enter Mount Path: ")
        print()
        system("mount {} {}".format(diskname, mntPath))
    elif ft.lower() == 'u':
        print("DISK LIST - \n")
        system("lsblk -a")
        print("\nUNMOUNT DISK - \n")
        path = input("Enter Disk or Path to unmount: ")
        print()
        system("umount {}".format(path))
    else:
        print("Enter M or U")
        mountUmountDisk()

def listPVs():
    system("pvdisplay")

def listVGs():
    system("vgdisplay")

def listLVs():
    system("lvdisplay")
    
def createPV():
    print("DISK LIST - \n")
    system("fdisk -l | grep 'Disk /'")
    print("\nCREATE PV - \n")
    disknames = input("Enter Disk Names (Seperate by Space if multiple): ")
    print()
    system("pvcreate {}".format(disknames))
    
def createVG():
    print("PV LIST - \n")
    system("pvdisplay -C")
    print("\nCREATE VG - \n")
    vgname = input("Enter VG Name: ")
    pvnames = input("Enter PV Names (Seperate by Space if multiple): ")
    print()
    system("vgcreate {} {}".format(vgname,pvnames))

def createLV():
    print("VG LIST - \n")
    system("vgdisplay -C")
    print("\nCREATE LV - \n")
    lvname = input("Enter LV Name: ")
    vgnames = input("Enter VG Name (Seperate by Space if multiple): ")
    lvsize = input("Enter LV Size: ")
    print()
    system("lvcreate --size {} --name {} {}".format(lvsize, lvname, vgnames))

def extendVG():
    print("VG LIST - \n")
    system("vgdisplay -C")
    print("PV LIST - \n")
    system("pvdisplay -C")
    print("\nREDUCE VG - \n")
    vgname = input("Name of VG to Extend: ")
    pvname = input("Enter PV Name to Add: ")
    print()
    system("vgextend {} {}".format(vgname, pvname))

def reduceVG():
    print("VG LIST - \n")
    system("vgdisplay -C")
    print("PV LIST - \n")
    system("pvdisplay -C")
    print("\nREDUCE VG - \n")
    vgname = input("Name of VG to Reduce: ")
    pvname = input("Enter PV Name to Remove: ")
    print()
    system("vgreduce {} {}".format(vgname, pvname))
    
def extendLV():
    print("LV LIST - \n")
    system("lvdisplay -C")
    print("\nEXTEND LV - \n")
    lvname = input("Enter LV Name: ")
    size = input("Enter Size to Extend (nM = nMB): ")
    print()
    system("lvextend -L+{} {}".format(size,lvname))

def reduceLV():
    print("LV LIST - \n")
    system("lvdisplay -C")
    print("\nEXTEND LV - \n")
    lvname = input("Enter LV Name: ")
    size = input("Enter Size to Reduce (nM = nMB): ")
    print()
    system("lvreduce -L-{} {}".format(size,lvname))

def movePV():
    print("PV LIST - \n")
    system("pvdisplay -C")
    print("\nMOVE PV - \n")
    oldpv = input("Enter Old PV Name: ")
    newpv = input("Enter New PV Name: ")
    print()
    system("pvmove {} {}".format(oldpv,newpv))
    
def removePV():
    print("PV LIST - \n")
    system("pvdisplay -C")
    print("\nREMOVE PV - \n")
    pvname = input("Enter PV Name: ")
    print()
    system("pvremove {}".format(pvname))

def removeVG():
    print("VG LIST - \n")
    system("vgdisplay -C")
    print("\nREMOVE VG - \n")
    vgname = input("Enter VG Name: ")
    print()
    system("vgremove {}".format(vgname))

def removeLV():
    print("LV LIST - \n")
    system("lvdisplay -C")
    print("\nREMOVE LV - \n")
    lvname = input("Enter LV Name: ")
    print()
    system("lvremove {}".format(lvname))
