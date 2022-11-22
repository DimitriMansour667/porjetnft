def addNew():
    file = open("data.txt", "r+")
    nftname = input("NFT NAME : ")
    nftimg = input("NFT IMG : ")
    nftOwner = input("NFT OWNER (x if no owner) : ")
    file.write(nftname + " " + nftimg + " " + nftOwner + "\n")
    file.close

def moveNft():
    file = open("data.txt", "r+")
    file.close

action = None
while(action != "3") : 
    action = input("\t NFT PROJECT\n1- ADD NEW NFT\n2- MOVE NFT\n3- CLOSE\n")
    if(action == "1") :
        addNew()
    elif(action == "2") :
        moveNft()
    

    