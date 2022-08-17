import locale
import calendar

##Simple calendar in CZ lang


locale.setlocale(locale.LC_ALL, 'cs_CZ.UTF-8')

c = calendar.TextCalendar(calendar.MONDAY)
c.pryear(2022)