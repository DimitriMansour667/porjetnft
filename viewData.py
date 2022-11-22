import pickle
with open("data", "rb") as fp:   # Unpickling
    b = pickle.load(fp)
print(b)