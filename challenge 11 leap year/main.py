def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True;
            else:
                return False;
        else:
            return True;
    else:
        return False;


def days_in_month(y, m):
    if is_leap(y):
        print(f"Year {y} is a leap year")
    else:
        print(f"Year {y} is not a leap year")

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    if (m == 2 and is_leap(y)):
        return 29;
    else:
        return month_days[m - 1];


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(f"month {month} has {days} days in year {year}")
