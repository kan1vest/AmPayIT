employees = [
  {"name": 'Иван', "position": 'разработчик' , "salary": 55000},
  {"name": 'Анна', "position": 'аналитик' , "salary": 48000},
  {"name": 'Петр', "position": 'тестировщик' , "salary": 52000},
]



def process_employees(employees):
   high_paid_employees = [employee['name'] for employee in employees if employee['salary'] > 50000]
   average_salary = sum(employee['salary'] for employee in employees) / len(employees)
   sorted_employees = sorted(employees, key=lambda employee: employee['salary'], reverse=True)
   return high_paid_employees, average_salary, sorted_employees


print(process_employees(employees))
