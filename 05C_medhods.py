MyDict = {
"fast" :"please run fast",
"abhishek" :"is a good boy",
"marks" :[1,2,34,5],
"abhi" : {"ku": "kumar"},
1:2
}
print(MyDict.keys())#print the key of the dictionary

print(list(MyDict.keys()))
print(MyDict.values())#print the values of the dictionary
print(MyDict.items())#prints the keys+value  of the dictionary of the content

updateDict={
    "kancan":"sister",
     "ankit":"brother",
     "abhishek":"is a student & live in bareilly"
}
MyDict.update(updateDict)#update the dictionary by adding key-value paires form updateDict
print(MyDict)
print(MyDict.get("abhishek2"))#Return none value if key is not present in the dictionary

print(MyDict["abhishek2"])#throws an error as abhishek2 is not a present in the dictionary



