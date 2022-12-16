def convert(fraction_inp):
    fraction = fraction_inp.split("/")
    return 100*(int(fraction[0])/int(fraction[1]))

def gauge(percent):
        if percent == 100:
            return "F"
        elif percent == 0:
            return "E"
        else:
            return str(int(percent))+"%"



error = True
while error:
    fraction_inp = input("Fraction: ")
    try:
        print(gauge(convert(fraction_inp)))
        error = False
    except (ValueError,ZeroDivisionError):
        error = True

