"""
There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.

"""


def recoverSecret(triplets):
    # 'triplets is a list of triplets from the secrent string. Return the string.'

    letters = list(set([l for t in triplets for l in t]))        
            
    for t in triplets * len(letters):
        for i in range(len(t)-1):
            a, b = letters.index(t[i]), letters.index(t[i+1])
            if( a > b ): letters[b], letters[a] = letters[a], letters[b]
            
    return ''.join(letters)