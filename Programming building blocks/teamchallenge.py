# first_name = input('First name: ')
# last_name = input('Last name: ')
# email = input('Email address: ')
# phone = input('Phone number: ')
# job_title = input('Job title: ')
# id_number = input('ID number: ')
hair = input('Hair Color: ')
eye_color = input('Eye color: ')
month_started = input('Enter month started working:')
training = input('Have you completed your training? ')
# print()
# print('The ID Card is:')
# print('-----------------------------------------')
# print(last_name.upper() + ',' , first_name)
# print(job_title)
# print('ID:', id_number)
# print()
# print(email)
# print(phone)
# print()
print('Hair:', hair, '{:>20}'.format('Eyes:'), eye_color)
print('Month: ', month_started, '{:>20}'.format('Training:'), training)

print('-----------------------------------------')