import pickle


def addNew():
    data = load()
    nftname = input("NFT NAME : ")
    nftimg = input("NFT IMG : ")
    nftOwner = input("NFT OWNER (x if no owner) : ")
    newNft = [nftname, nftimg, nftOwner]
    data.append(newNft)
    save(data)

def editNft():
    data = load()
    search = input("NFT name : ")
    result = findIndex(data, search)
    print("\t\tSELECTED NFT")
    print(data[result[0]])
    save(data)




action = None
while(action != "3") : 
    action = input("\t\tNFT PROJECT\n1- ADD NEW NFT\n2- MOVE NFT\n3- CLOSE\n")
    if(action == "1") :
        addNew()
    elif(action == "2") :
        editNft()
        
        
def findIndex(stringArr, keyString):
 
    #  Initialising result array to -1
    #  in case keyString is not found
    result = []
 
    #  Iteration over all the elements
    #  of the 2-D array
 
    #  Rows
    for i in range(len(stringArr)):
 
        #  Columns
        for j in range(len(stringArr[i])):
            #  If keyString is found
            if stringArr[i][j] == keyString:
                result.append(i)
                result.append(j)
                return result
    result.append(-1)
    result.append(-1)
    #  If keyString is not found
    #  then -1 is returned
    return result

def load() :
    with open("data", "rb") as fp:   # Unpickling
        return pickle.load(fp)
    
def save(data) :
    with open("data", "wb") as fp:   #Pickling
        pickle.dump(data, fp)
    