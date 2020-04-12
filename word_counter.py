def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count
s = input("Enter String Here : ")
print(word_counter(s))