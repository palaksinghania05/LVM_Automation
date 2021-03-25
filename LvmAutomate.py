import os
import getpass

os.system("tput setaf 3")
print("\t\t\tWelcome to LVM Automation !!")
os.system("tput setaf 7")
print("\t\t\t_______________________________________________")

password = getpass.getpass("Enter your password : ")
if password != "redhat":
    print("Incorrect Password !!")
    exit()

while True:
    os.system("clear")
    print(""" \n 
        Press 1 : To check storage attached
        Press 2 : To create and display Physical Volume
        Press 3 : To create and display Volume Group
        Press 4 : To create and display Logical Volume
        Press 5 : To format Logical Volume'
        Press 6 : To mount logical volume to directory and check if successfully attached
        Press 7 : To extend LV and display
        Press 8 : To Exit""")

    ch = input("Enter your choice: ")

    if int(ch) == 1:
        os.system("fdisk -l")

    elif int(ch) == 2:
        pv = input("Enter the name of device : ")
        os.system("pvcreate {}".format(pv))
        os.system("pvdisplay {}".format(pv))

    elif int(ch) == 3:
        vgn = input("Enter volume group name : ")
        pv = input("Enter the name of device : ")
        os.system("vgcreate {} {}".format(vgn, pv))
        os.system("vgdisplay {}".format(vgn))

    elif int(ch) == 4:
        size = input("Enter size for your logical volume : ")
        lv = input("Enter Logical Volume name : ")
        vgn = input("Enter volume group name : ")
        os.system("lvcreate --size {} --name {} {}".format(size, lv, vgn))
        os.system("lvdisplay /dev/{}/{}".format(vgn, lv))

    elif int(ch) == 5:
        lv = input("Enter Logical Volume name : ")
        vgn = input("Enter volume group name : ")
        os.system("mkfs.ext4 /dev/{}/{}".format(vgn, lv))

    elif int(ch) == 6:
        folder = input("Enter path of directory on which you wish to mount your lv : ")
        lv = input("Enter Logical Volume name : ")
        vgn = input("Enter volume group name : ")
        os.system("mount /dev/{}/{} {}".format(vgn, lv, folder))
        os.system("df -h")

    elif int(ch) == 7:
        lv = input("Enter Logical Volume name : ")
        vgn = input("Enter volume group name : ")
        size = input("Enter new size you want for your lv : ")
        os.system("lvextend --size +{} /dev/{}/{}".format(size, vgn, lv))
        os.system("resize2fs /dev/{}/{}".format(vgn, lv))
        os.system("df -h")

    elif int(ch) == 8:
        exit()

    else:
        print("Invalid choice !")

    input("Press Enter to continue..")
    print("\n")





