#~ Day 1: Basic String Operations

User = input ("Enter Message: ") 
print(len(User),"\n",User.lower()) 
arr = User.split() 
print(arr)

'''Sample Input/Output
Enter Message: I LOve NLP 
10 
i love nlp 
['I', 'LOve', 'NLP' ]'''