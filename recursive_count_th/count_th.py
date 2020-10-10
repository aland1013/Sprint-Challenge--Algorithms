'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case
    # if there are less than 2 letters left in
    # word, we are done looking for 'th'
    if len(word) < 2:
        return 0
    
    # grab first two letters in word 
    slice = word[0:2]
    
    # check and see if they equal 'th'
    # if they do, return 1 plus a recursive
    # call to count_th, passing in everything
    # but the first letter in word
    if slice == 'th':
        return 1 + count_th(word[1:])
    
    # if the first two letters do not equal 'th'
    # drop the first letter from word and make a 
    # recursive call to count_th 
    return count_th(word[1:])
