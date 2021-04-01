#content_file = open("continents.txt")
#myfile = content_file.read()
#content_file.close()
#print(myfile)

#with open("files/continents.txt","r") as content_file:
#    myfile = content_file.read()
#    print(myfile)

with open("files/continents.txt","a+") as content_file:
    content_file.write("\nAsia")
    content_file.seek(0)
    myfile = content_file.read()
    print(myfile)