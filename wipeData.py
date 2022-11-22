
import pickle
data = []
with open("data", "wb") as fp:   #Pickling
    pickle.dump(data, fp)
with open("data", "rb") as fp:   # Unpickling
    data = pickle.load(fp)
print(data)