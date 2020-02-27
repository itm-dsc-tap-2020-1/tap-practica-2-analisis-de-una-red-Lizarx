import os
hostname = "www.itmorelia.edu.mx"

respuesta = os.system("ping -c 1 "+hostname)
if(respuesta==0):
    print(hostname + ": está en funcionamiento!")
else:
    print(hostname + ": No esta en funcionamiento")
red = "200.33.171.0/24"
os.system("nmap -sP "+red)

"""
christian@christian-Inspiron-5558:~$ /usr/bin/python3 /home/christian/Escritorio/Escuela/Tap/Practica2.py
PING denebvirtual.itmorelia.edu.mx (200.33.171.77) 56(84) bytes of data.
64 bytes from denebvirtual.itmorelia.edu.mx (200.33.171.77): icmp_seq=1 ttl=63 time=0.699 ms
#Con ping
*** --- denebvirtual.itmorelia.edu.mx ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.804/0.804/0.804/0.000 ms
www.itmorelia.edu.mx: está en funcionamiento!

#Con nmap
Starting Nmap 7.60 ( https://nmap.org ) at 2020-02-27 11:36 CST
Nmap scan report for 200.33.171.3
Host is up (0.00082s latency).
Nmap scan report for 200.33.171.13
Host is up (0.00083s latency).
Nmap scan report for 200.33.171.85
Host is up (0.00089s latency).
Nmap scan report for 200.33.171.115
Host is up (0.0010s latency).
Nmap scan report for 200.33.171.120
Host is up (0.00068s latency).
Nmap scan report for 200.33.171.124
Host is up (0.0075s latency).
Nmap done: 256 IP addresses (6 hosts up) scanned in 19.73 seconds"""