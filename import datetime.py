#IMPORTED DATE/TIME LIBRARY
#GETTING THE CURRENT DATE AND TIME
import datetime
now = datetime.datetime.now()

#DATE/TIME FORMAT FOR OUTPUT
present_date = now.strftime("%Y-%m-%d")
present_time = now.strftime("%H:%M:%S")
week_day = now.strftime("%A")

#
print(f"Present Date: {present_date}")
print(f"Present Time: {present_time}")
print(f"Day of the week: {week_day}")