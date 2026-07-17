#this program demonstrates various set operations
baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])
#displays members of the basketball team
print('The following students are on the baseball team:')
for name in baseball:
    print(name)
#displays members of the baseball team
print()
print('The following students are on the basketball team:')
for name in basketball:
    print(name)

#demonstrates intersection
print()
print('the following students play both baseball and basketball: ')
for name in baseball.intersection(basketball):
    print(name)

#demonstrates union
print()
print('The following students play either baseball or basketball:')
for name in baseball.union(basketball):
    print(name)

#demonstrate difference of baseball and basketball
print()
print('The following students play basketball but not baseball:')
for name in basketball.difference(baseball):
    print(name)

#demonstrates symmetric difference
print()
print('the following students play one sport, but not the other')
for name in baseball.symmetric_difference(basketball):
    print(name)
