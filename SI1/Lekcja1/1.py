import datetime

y = datetime.datetime.now()
x = y.strftime("%j")
print("Dzisiaj jest " + x[1:3] + " dzień w 2019r")
