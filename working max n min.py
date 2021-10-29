def rps(a,b):


        if (a=="s" and b=="p") or (a=="p" and b=="r") or (a=="r" and b=="s"):
            print("A won")


        elif a==b :
            print("draw")

        else:
            print("b won")

while True:

    a = input("P1--s/r/p/quit")
    b = input("P2--s/r/p/quit")
    if a == "quit":
        break
    if b == "quit":
        break
    rps(a,b)
