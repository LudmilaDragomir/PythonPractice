# Definition:
# Your friend works for an antique book shop that sells books between 1800 and 1950 and wants to
# quickly categorise books by the century and decade that they were written.
# Write a program that takes a year (e.g. 1872)
# and outputs the century and decade (e.g. "Nineteenth Century, Seventies")

from num2words import num2words

centuries = {18: 'Eighties', 19: 'Nineteenth', 20: 'Twentieth'}

decades = {10: 'Tens', 20: 'Twenties',
           30: 'Thirties', 40: 'Forties',
           50: 'Fifties', 60: 'Sixties',
           70: 'Seventies', 80: 'Eighties',
           90: 'Nineties', 00: 'Hundreds'}

print('*********************!')
print('The antique book shop!')
print('*********************!')


# Most common usage of num2words
# print(num2words(20))
# print(num2words(36, to='ordinal'))
# print(num2words(20, to='ordinal_num'))
# print(num2words(36, to='year'))
# print(num2words(36, to='currency'))

# Language Support.
# print(num2words(36, lang='es'))


def century_from_year(year):
    century = year // 100 + 1
    return century


def decade_from_year(year):
    decade = year % 100 // 10 * 10
    return decade


def century_and_decade(year):
    century = century_from_year(year)
    decade = decade_from_year(year)
    # cent_decade = divmod(year, 100)
    century = centuries[century]
    decade = decades[int(decade)]
    # print('{}, {}'.format(centuries[cent_decade[0] + 1] + " Century", round(cent_decade[1], -1)))
    print('{}, {}'.format(century + " Century", decade))


year = input('Introduce the year of the book: ')
century_and_decade(int(year))
