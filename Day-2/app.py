#~ Tokenzation

txt = "Hello!!!   NLP??  is  cool."


def process(string):
    pun = ""
    for char in string:
        if char.isalnum() or char.isspace():
            pun += char

    return pun


cleanTxt = process(txt)
token = cleanTxt.split()
print(f"{token}\n No of Tokens: {len(token)}")


'''Sample Output
output: ['Hello', 'NLP', 'is', 'cool'] 
No of Tokens: 4
'''