def rev(s):
    s1=s[::-1]
    return s1
def count_vowel(s):
    count=0
    for i in s:
        if i.lower() in 'aeiou':
           count+=1
    return count
def palindrome(s):
    s1=s[::-1]
    if s==s1:
        print('The string is a palindrome')
    else:
        print('The string is not a palindrome')
