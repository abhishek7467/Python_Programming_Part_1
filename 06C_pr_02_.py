text = input("Enter you text")
spam=False
if("make a lot of money" in text):
    spam=True
elif ("buy now " in text):
    spam=True
elif("click this"in text):
    spam=True
else:
    print("this is a not a spam")    
if(spam):
    print("this is a spam")
else:
    print("this is not a spam ")           