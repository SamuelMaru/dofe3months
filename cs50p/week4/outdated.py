months = [
        "",
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
month = day = year = ""

while True:
        date = input("Date: ")
        if "/" in date:
            month, day, year = date.split("/")
        else:
            month, day, year = date.replace(",","").split()
            if month in months:
                month = months.index(month)
            else:
                pass
        try:
            day = int(day)
            year = int(year)
            month = int(month)
            if day > 31 or month > 12:
                pass
        except ValueError:
            pass
        break

print(f"{year}-{month:02}-{day:02}")
