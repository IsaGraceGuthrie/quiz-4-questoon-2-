#the authors name is Isa Grace Guthrie
def hash_spam(x):
    index=0
    count=0
    while index<len(x):
        if x[index:index+len("#")]=="#":
            index+=1
            count+=1
        else:
            index+=1
    print(count)
    if count>=4:
        print("This tweet will be considered as a spam!")
    else:
        return None
    

string="I am incredible #happy #today hope you have a great #day"
hash_spam(string)

