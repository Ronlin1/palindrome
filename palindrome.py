# A palindrome is a word, number, phrase, or
# other sequence of characters which reads
# the same backward as forward, such as
# madam, racecar, civic, Dad, Mum, pop,

# def palindrome()
def palindrome(sequence):
    # for loop for panctuation
    for i in (",!,(){}[]'><&$@.'"):
        if i in sequence:
            sequence = sequence.remove(i)
    # palindrome varibale
    palindrome = []
    words = sequence.split(' ')
    # for loop
    for word in words:
        # check for palindrome
        word = word.lower()
        if word == word[::-1]:
            palindrome.append(word)
    # return palindrome
    return palindrome

print(palindrome("My Mum has gone to see D ad with a racecar"))
