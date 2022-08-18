"""
Python3.X Script.
Author : Pavan Jim
Outcome desired : Find the day that corresponds to the given date.

Method from:
- https://lehollandaisvolant.net/?d=2015/05/23/17/09/56-geek-calculer-le-jour-de-la-semaine-pour-nimporte-quel-date-de-tete

Procedure :
    - Check if the date is writed in the expected format
    - Check if the date can exists and included in the calendar
    - Launch the algorithm
    - Get the day
"""


from re import search


def date_filter(date):
    """Check if the date follows the desired pattern and return it"""

    return search("(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9])/[0-9]{4}", date)


def is_rational_date(dd, mm, yy):
    """Check if the date can exists"""

    if mm == 2:
        if is_bissextile(yy):
            if dd < 30:
                return True
        else:
            if dd < 29:
                return True

    elif dd <= month_refer[mm-1]:
        return True


def explode(date):
    """Return the day, month, year numbers"""
    
    return list(map(int, date.split("/")))


def get_day_num(dd, mm_code, yy_code):
    """Get the day number"""

    return (dd%7 + yy_code%7 + mm_code)%7


def get_year_code(yy):
    """Get the code that corresponds to the year,
    according to the website method"""

    y = yy % 100

    if yy < 2000:
        code = int((y - y / 4) % 7) + 1
    else:
        code = int((y + y / 4) % 7)

    return code


def get_month_code(mm, yy):
    """Get the code that corresponds to the month"""

    if is_bissextile(yy):
        if mm == 1 or mm == 2:
            mm -= 1

    return months_code[mm-1]


def is_bissextile(yy):
    """Check for leap years"""

    if yy % 4 == 0 and yy % 100 != 0:
        return True
            
    elif yy % 400 == 0:
        return True


def process(date):
    """Lanch the algorithm to find the date"""

    date = date_filter(date)

    if date:
        dd, mm, yy = explode(date.group())

        if is_rational_date(dd, mm, yy):
            mm_code = get_month_code(mm, yy)
            yy_code = get_year_code(yy)
            num_day = get_day_num(dd, mm_code, yy_code)

            return days_refer[num_day]
        

month_refer = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_code = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

days_refer = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

if __name__ == "__main__":
    #Exemple : "01/09/2018"

    while True:
        date = input("Enter a date : ")
        day = process(date)
            
        print("the date chosen : {0} corresponds to {1}".format(date, day))
