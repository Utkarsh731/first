vowel=['a','e','i','o','u','A','E','I','O','U']
cha=input()
if ((cha >= 'a' and cha <= 'z') or (cha >= 'A' and cha <= 'Z')):
    if cha in vowel:
        print('Vowel')
    else:
        print('Consonant')
else:
    print('Invalid')
