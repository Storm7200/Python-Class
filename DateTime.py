def DateTimeFunction():
import datetime
now = datetime.datetime.now()
print ("Current Date and Time : ")
print (now.strftime("%r"))
