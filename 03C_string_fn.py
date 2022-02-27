story="Once upon a time abhishek was a student and studies in future college"
print(story)
#string function
#1 lenght of string (how many no. of element in  the string)

#print(len(story))
#2
#print(story.endswith("ashj"))#this is wrong
#print(story.endswith("college"))#this is right

#3 count any no. of elements and word 
#print(story.count("a"))
#print(story.count("o"))
#print(story.count("college"))

#4 1st element convert in capital latter
#print(story.capitalize())

#5 find position of element and word
#print(story.find("college"))
#print(story.find("jhd"))#if output is -1 then this is not present in string

#6 replace any word 
#print(story.replace("college","school"))

#7 escape sequence character \n and tab \t
 
story="Once upon\\ a time abhishek was a student.\n and\t studies in future \ncollege"
print(story)
