#
#          DO NOT EDIT
#
#          THIS IS WHERE WE STORE THE SEPERATE PARTS,
#          THE ACTUAL PROGRAM IS AT main.py
#



SMALL_NUMBERS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
MULTIPLES_OF_TEN = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
POWERS_OF_THOUSAND = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion']

SMALL_THOUSAND_POWER_ROOTS = ['', 'm', 'b', 'tr', 'quadr', 'quint', 'sext', 'sept', 'oct', 'non', 'dec']
ADDITIVE_THOUSAND_POWER_ROOTS = ['', 'un', 'duo', 'tre', 'quattuor', 'quin', 'sex', 'septen', 'octo', 'novem']
TEN_THOUSAND_POWER_ROOTS = ['', 'dec', 'vigint', 'trigint', 'quadragint', 'quinquagint', 'sexagint', 'septuagint', 'octogint', 'nonagint']

def power_of_thousand(n):
    if n == 0:
        return ''
    n -= 1
    if n == 0:
        return 'thousand'
    if n < 10:
        return SMALL_THOUSAND_POWER_ROOTS[n] + 'illion'
    if n == 100:
        return 'centillion'
    return ADDITIVE_THOUSAND_POWER_ROOTS[n % 10] + TEN_THOUSAND_POWER_ROOTS[n // 10] + 'illion'

def convert_section(n, power):
    if n == 0:
        return
    if n >= 100:
        yield SMALL_NUMBERS[n // 100]
        yield 'hundred'
        if n % 100 != 0:
            yield 'and'
    n %= 100
    if 0 < n < 20:
        yield SMALL_NUMBERS[n]
    elif n != 0:
        yield MULTIPLES_OF_TEN[n // 10]
        if n % 10 != 0:
            yield SMALL_NUMBERS[n % 10]
    if power:
        yield power

def convert_number(n):
    parts = []
    power = 0
    done_and = False
    while n:
        section = '-'.join(convert_section(n % 1000, power_of_thousand(power)))
        if not done_and and n >= 1000 and section:
            if n % 1000 < 100:
                section = f'and-{section}'
            done_and = True
        if section:
            parts.append(section)
        n //= 1000
        power += 1
    if parts == []:
        return 'zero'
    return '-'.join(parts[::-1])

number = int(input("numer: "))
print(convert_number(number))
input()
