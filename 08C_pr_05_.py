def remove_and_split(string,word):
    new_str=string.replace(word,"")
    return new_str.strip()
Name= " Abhishek kumar is a good boy"
n=remove_and_split(Name,"Abhishek")
print(n)

    