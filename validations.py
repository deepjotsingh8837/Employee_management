def validate_employee_id(emp_id):
  if not emp_id.isdigit():
    return False
  return True


def validate_salary(salary):

  salary = float(salary)
  if salary < 0:
    return False
  else:
    return True


def validate_age(age):
  age = int(age)
  if age < 18 or age > 100:
    return False
  else:
    return True


def validate_gender(gender):
  if gender.lower() not in ['male', 'female', 'others']:
    return False
  return True


def validate_city(city):
  if not city.isalpha():
    return False
  return True


def validate_PAN(pan_card):
  if len(pan_card) != 10:
    return False

  for char in pan_card[:5]:
    if not char.isalpha() or not char.isupper():
      return False

  for char in pan_card[5:9]:
    if not char.isdigit():
      return False

  if not pan_card[9].isalpha() or not pan_card[9].isupper():
    return False

  return True


def validate_aadhar(aadhar):
  if len(aadhar) != 12:
    return False

  if not aadhar.isdigit():
    return False
  return True


def validate_phone_number(phone):
  if len(phone) != 10:
    return False
  if not phone.isdigit():
    return False
  return True


def validate_name(name):
  words = name.split(" ")
  if len(words) > 3 or len(words) < 1:
    return False
  elif "".join(words).isalpha() == False:
    return False
  else:
    for p in words:
      if p.istitle() == False:
        return False
  return True


def validate_department(department):
  if department.lower() not in [
      'it', 'sales', 'finance', 'hr', 'transportation'
  ]:
    return False
  return True


def validate_designation(designation):
  if designation.lower() not in [
      'manager', 'developer', 'hr', 'driver', 'sales_executive', 'associate_hr'
  ]:
    return False
  return True


def validate_dob(dob):
  l = dob.split('/')
  dd = int(l[0])
  mm = int(l[1])
  yy = int(l[2])
  if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12:
    max_days = 31
  elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
    max_days = 30
  elif yy % 4 == 0 and yy % 100 != 0 or yy % 400 == 0:
    max_days = 28
  else:
    max_days = 29
  if mm < 1 or mm > 12:
    return False
  elif dd < 1 or dd > max_days:
    return False
  else:
    return True
