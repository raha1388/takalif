import numbers
import random

print("sang,kaghaz,gheachi")

user=input("sang ya kaghaz ya gheachi:")

number=random.randint(1,3)

bazikon=""

if number==1:
    bazikon="sang"
    print("sang")
elif number==2:
    bazikon="kaghaz"
    print("kaghaz")
elif number==3:
    bazikon="gheachi"
    print("gheachi")

if bazikon=="sang" and user=="kaghaz":
    print("bakhti")
elif bazikon=="sang" and user=="gheachi":
    print("bordi")
elif bazikon=="kaghaz" and user=="sang":
    print("bordi")
elif bazikon=="kaghaz" and user=="gheachi":
    print("bakhti")
elif bazikon=="gheachi" and user=="kaghaz":
    print("bordi")
elif bazikon=="ghachi" and user=="sang":
    print("bakhti")
