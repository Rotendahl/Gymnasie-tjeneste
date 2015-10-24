mesg = "Benjamin er sej, og coding pirates er sjovt"
ks   = [20]
mode = "e"


def encrypt(msg,mode):
    newMesg = ""
    k = 0
    for i in range(0,len(msg)):
        if mesg[i].isalpha():
            letter  = ord(mesg[i]) - 97
            enCrypt = chr(((letter + ks[k % len(ks)])%26)+97)
            deCrypt = chr(((letter - ks[k % len(ks)])%26)+97)
            newletter = enCrypt if mode =='e' else deCrypt
            k+= 1
            newMesg = newMesg + newletter
        else:
            newMesg = newMesg + " "
    return newMesg

print encrypt(mesg, mode)
