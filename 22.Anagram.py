def anagram(str1,str2):
    if(sorted(str1)==sorted(str2)):
        return True
    else:
        return false
str1=input()
str2=input()
if anagram(str1,str2):
    print("Anagram")
else:
    print("It is not a anagram")
