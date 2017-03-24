vowels = "aeiou"
word = raw_input("Enter a word('.' to exit):")
while word != '.':
    start = word[0]
    if start in vowels:
        word += "yay"
        print word
    else:
        for index in range(1,len(word)-1):
            if word[index] in vowels:
                lword = word[0:index] + "ay"
                rword = word[index:]
                word = rword + lword
                print word
                break
    word = raw_input("Enter a word('.' to exit):")
