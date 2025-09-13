def check_leap_year(year):
        if year % 100 and year % 400 or not year % 100 and year % 4:
            return True
        else:
             return False
            
