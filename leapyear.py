year=int(input())
def leapyear(year):
    leap='no'
    if year%4==0 and year%100!=0:
        leap='yes'
    elif year%100==0 and year%400==0:
        leap='no'
    return leap
print(leapyear(year))
