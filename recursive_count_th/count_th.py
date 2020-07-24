'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # Use recursion - REQURED -NO LOOPS
    # case matters
    #for every word, find every occurence of 'th'
    #if t and h are not next to each other, ignore
    # if t and h ARE next to each other, calculate the number of 'th' in that word
        # note - if they must be consecutive, check in steps of two?
    # return that number
    
    # # make sure word parameter has more than 0 characters
    if len(word) == 0:
        return 0
       
    # word has characters
    else:
        #initialize count
        count = 0
        # steps of 2
        if word[0:2] == "th":
            count += 1

    return count + count_th(word[1:])




