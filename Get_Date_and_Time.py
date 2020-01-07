import datetime
now = datetime.datetime.now() #stores our code in the variable "now"
print('Current date and time: ')
print(now.strftime("%Y-%m-%d %H:%M:%S")) #'now.strftime' formats the numbers from the datetime module and turns them in strings.
