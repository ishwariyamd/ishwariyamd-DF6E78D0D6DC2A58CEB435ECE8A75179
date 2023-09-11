def isleapyear(year):
  if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    return True
  else:
    return False


year = 2005
if isleapyear(year):
  print("2005 is a leap year".format(year))
else:
  print("2005 is not a leap year".format(year))
