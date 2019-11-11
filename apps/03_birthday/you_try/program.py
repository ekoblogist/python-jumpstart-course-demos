import datetime


def header():
    print(30*'-')
    print('       MY BIRTHDAY APP')
    print(30*'-')
    print()

def date_of_the_birth():
    print('How old are you?')
    year = int(input('What year were you born in [YYYY]? '))
    month = int(input('What month were you born in [MM]? '))
    day = int(input('What day were you born on [DD]? '))

    birthday = datetime.date(year, month, day)

    return birthday


def current_date():
    today = datetime.date.today()
    return today


def days_until_birthday(today, birthday):
    this_year_birthday = datetime.date(today.year, birthday.month, birthday.day)
    days = this_year_birthday - today
    return days


def main():
    header()
    bday = date_of_the_birth()
    print(bday)
    today = current_date()
    print(today)
    days_u_b = days_until_birthday(today, bday)
    print(days_u_b.days)


main()