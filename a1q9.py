m1 = input('Enter marks of 1 : ')
m2 = input('Enter marks of 2 : ')
m3 = input('Enter marks of 3 : ')
m4 = input('Enter marks of 4 : ')
m5 = input('Enter marks of 5 : ')
perc = (m1+m2+m3+m4+m5)*100/500
if perc<35 :
    print'Student has Failed!!!!, with percentage of',perc
else :
    print'Student has PAssedd!!!, with percentage of',perc
