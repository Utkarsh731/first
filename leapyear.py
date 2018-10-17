year=int(input())
def leapyear(year):
    leap='No'
    if year%4==0 and year%100!=0:
        leap='Yes'
    elif year%100==0 and year%400==0:
        leap='No'
    return leap
print(leapyear(year))
