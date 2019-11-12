import datetime


def header():
    print(30*'-')
    print('       MY BIRTHDAY APP')
    print(30*'-')
    print()


def date_of_the_birth():
    print("When's your birthday?")
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
    days_u_b = days.days
    return days_u_b


def main_text(birthday, days):
    print(f'Looks like you were born on {birthday.day}/{birthday.month}/{birthday.year}')
    if days > 0:
        print(f'Your birthday is in {days} days.')
    elif days < 0:
        print(f'Your birthday was {-days} days ago.')
    else:
        print('Happy birthday!!!')


def main():
    header()
    bday = date_of_the_birth()
    today = current_date()
    days_u_b = days_until_birthday(today, bday)
    main_text(bday, days_u_b)



main()