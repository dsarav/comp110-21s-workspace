"""A vaccination calculator."""

__author__ = "730318366"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population: "))
doses: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
percent: int = int(input("Target percent vaccinated: "))

today: datetime = datetime.today()
days: timedelta = timedelta(int(doses / doses_per_day))
days_remaining: datetime = today + days

print("We will reach",percent,"% vaccination in",int(doses / doses_per_day),"days, which falls on", days_remaining.strftime("%B %d, %Y"))
