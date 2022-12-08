import subprocess
import re

first_ip = input("Enter the first ip address: ")
last_ip = input("Enter the last ip address: ")

def Get_Host(x):
    Dot_Counter = 0
    Pos_Counter = 0
    for i in x:
        if i == ".":
            Dot_Counter = Dot_Counter +1
        if Dot_Counter == 3:
            return (x[0:Pos_Counter +1], x[Pos_Counter+1: ])
            break
        Pos_Counter +=1

Network, First_Host = Get_Host(first_ip)
Network, Last_Host = Get_Host(last_ip)

Empty_String = ""

Counter = 0

for i in range(int(First_Host), int(Last_Host) +1):
    process = subprocess.getoutput("ping -n 1 " + Network + str(i))
    Empty_String += process

    String_Needed = re.compile(r"TTL=")
    mo = String_Needed.search(Empty_String)
    try:
        if mo.group() == "TTL=":
            print("Host " + Network + str(i) + "is UP")
    except:
        print("Host " + Network + str(i) + "is DOWN")

    Empty_String = ""

print("completed.")
