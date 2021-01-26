import uuid

rand_str = uuid.uuid4().hex[:6]

registration_from_data = {
  'email': f'prasanna.testingclub{rand_str}@gmail.com',
  'password': f'pass{rand_str}word',
  'first_name': 'prasanna',
  'last_name': f'{rand_str}',
  'username': f'prasanna{rand_str}suman',
  'about_me': f'{rand_str} is cool',
  'gender': 'male',
  'hobbies': ('travel', 'cooking', 'coding')
}

user_email = 'prasanna.testingclub@gmail.com'
