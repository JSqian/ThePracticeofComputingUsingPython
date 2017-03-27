def areAnagrams(word1,word2):
    '''
    Return true, if words are anagrams.'''
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)

    return word1_sorted == word2_sorted

print "Anagrams Test"

twoWords = raw_input("Enter two words: ")
word1,word2 = twoWords.split()

if areAnagrams(word1,word2):
    print "The words are anagrams."
else:
    print "The words are not anagrams."
