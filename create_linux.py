import os
os.system("cls")
print("Hello! Welcome to NeonDevelopment's Server creation script!")
print("Please enter one of the following server types to continue: ")
print("Vanilla, Spigot, CraftBukkit, Paper, BungeeCord, or FlameCord")
typerandom = input("Please enter a server type: ")
print("Example for server version: 1.16.4.\nFor BungeeCord & FlameCord, The latest version will be installed. This does not matter. ")
version = input("Please enter a server version: ")
serverram = input("Please enter an amount of ram for the server in GIGABYTES: ")
jartype = typerandom.lower()

# Code to wget the url and download the jar

#os.system("wget https://hostingfiles.gq/jars/" + jartype + "/release/" + jartype + "-" + version + ".jar")


os.system("cls")
if not os.path.exists('eula.txt'):
    print("Downloading jar...")
    if jartype == "spigot":
        os.system("wget https://hostingfiles.lol/jars/spigot/spigot-" + version + ".jar")
    elif jartype == "paper":
        os.system("wget -O paper-" + version + ".jar " + "https://hostingfiles.gq/jars/papermc/papermc-" + version + ".jar")
    elif jartype == "craftbukkit":
        os.system("wget https://hostingfiles.lol/jars/craftbukkit/craftbukkit-" + version + ".jar")
    elif jartype == "vanilla":
        os.system("wget https://hostingfiles.lol/jars/vanilla/release/vanilla-" + version + ".jar")
    elif jartype == "bungeecord":
        os.system("wget https://hostingfiles.lol/jars/bungeecord/bungeecord-latest.jar")
    elif jartype == "flamecord":
        os.system("wget https://hostingfiles.lol/jars/flamecord/flamecord-latest.jar")
    else:
        print("Jar not found.")
        exit()
    print("Accepting eula...")
    os.system("wget https://raw.githubusercontent.com/WeLikeToCodeStuff/Minecraft-Server-Creater/main/configs/eula.txt")
    #os.mknod('eula.txt')
    #f= open("eula.txt","a")
    #f.write("eula=true")
    if jartype == "bungeecord":
        print("Saving start.sh")
        f= open("start.sh","a")
        f.write("#!/bin/bash\n" + "java -Xmx" + serverram + "G" + " -Xms" + serverram + "G" + " -jar bungeecord.jar")
        print("Starting Server...")
        os.system("java -Xmx" + serverram + "G" + " -Xms" + serverram + "G" + " -jar bungeecord.jar")
    elif jartype == "flamecord":
        print("Saving start.sh")
        f= open("start.sh","a")
        f.write("#!/bin/bash\n" + "java -Xmx" + serverram + "G" + " -Xms" + serverram + "G" + " -jar flamecord.jar")
        print("Starting Server...")
        os.system("java -Xmx" + serverram + "G" + " -Xms" + serverram + "G" + " -jar flamecord.jar")
    else:
        print("Saving start.sh")
        f= open("start.sh","a")
        f.write("#!/bin/bash\n" + "java -Xmx" + serverram + "G" + " -Xms" + serverram + "G" + " -jar " + jartype + "-" + version + ".jar")
        os.system("chmod +x start.sh")
        print("Starting server...")
        os.system("java -Xmx" + serverram + "G" + " -Xms" + serverram + "G" + " -jar " + jartype + "-" + version + ".jar")
else:
    print("Server Starting...")
    os.system("java -Xmx" + serverram + "G" + " -Xms" + serverram + "G" + " -jar " + jartype + "-" + version + ".jar")
