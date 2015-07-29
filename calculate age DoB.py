import time
from datetime import datetime

# Calculates age based on birthday. Does take into account if you have had a b-day yet, but only returns age in years.
# def calc_age():
#     age = raw_input("Please enter your date of birth (MM/DD/YYYY):")
#     convert_date = True
#     while convert_date is True:
#         try:
#             birth_date_converted = datetime.strptime(age, '%m/%d/%Y')
#             new_age = datetime.utcnow() - birth_date_converted
#             print int(new_age.days/365.2465)
#         except ValueError:
#             print "Please reenter your date of birth correctly."
#             time.sleep(1)
#             calc_age()
#         finally:
#             convert_date = False
#
# calc_age()



# Calculates age based on year alone. Does not take into account if you have had a b-day yet.
# def calc_age():
#     birth_year = int(raw_input("Please enter your year of birth:"))
#     this_year = datetime.today().year
#     age = this_year - birth_year
#     print age
#
# calc_age()
