"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""
def move_zeros(array):
    for each in array:
        if each==0:
            array.pop(array.index(each))
            array.append(0)
    return array