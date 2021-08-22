"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

"""
"""
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
"""

def pig_it(text):
    #your code here
    print (text)
    ans=""
    list = text.split()
    for each in list:
        ans=ans+each[1:]+each[0]+'ay'+' '
    print(ans)
    ans = ans[:-1]
    # -1 to remove the last added space
    # so that punctuation remains untouched
    print (text[-1])
    if  not text[-1].isalpha():
        return ans[:-2]
    else:
        return ans