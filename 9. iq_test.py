"""
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

Examples:
iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd

"""
"""
def iq_test(numbers):
    #your code here
    list = numbers.split()
    num=0
    for i in range(len(list)-1):
        if (int(list[i])%2) == (int(list[i+1])%2):
            num = int(list[i])%2
        if i==2:
            break
    
    for n in list:
        if int(n)%2 != num:
            return list.index(n)+1
"""
def iq_test(n):
    n = [int(i)%2 for i in n.split()]
    if n.count(0)>1:
        return n.index(1)+1
    else:
        return n.index(0)+1   