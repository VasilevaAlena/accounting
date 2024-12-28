from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from random_strings import random_string


r = random_string(15)
print(r)


if __name__ == '__main__':
    current_date = datetime.now().strftime('%Y-%m-%d')
    print(current_date)
    calculate_salary()
    get_employees()
