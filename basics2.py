mylist = [100,123,142,-100,-154,152,195]
#newlist = [i/10 for i in mylist if i>0]
newlist = [i/10 if i>0 else 0 for i in mylist]

print(newlist)