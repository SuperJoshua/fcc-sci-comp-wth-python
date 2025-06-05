def add_time(start, duration, start_day = ''):
   days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

   start_time, meridiem = start.split()
   start_hour, start_minute = start_time.split(':')
   duration_hour, duration_minute = duration.split(':')

   a = int(start_hour)
   if (a < 12 and meridiem == 'PM'):
      a += 12
   elif (a == 12 and meridiem == 'AM'):
      a = 0 
   b = int(start_minute)
   x = int(duration_hour)
   y = int(duration_minute)

   new_meridiem = 'AM'
   days_plus = 0
   new_hour = a + x
   new_minute = b + y
   if (new_minute >= 60):
      new_minute %= 60
      new_hour += 1
   if (new_hour >= 24):
      days_plus = new_hour // 24
      new_hour %= 24
   if (new_hour > 11):
      new_meridiem = 'PM'
   if (new_hour > 12):
      new_hour -= 12
   if (new_hour == 0):
      new_hour = 12

   day = ''
   day_index = -1
   new_day = ''
   new_day_index = -1
   if (start_day):
      day = start_day[0].upper() + start_day[1:].lower()
      day_index = days.index(day)
      new_day_index = day_index + days_plus
      if (new_day_index >= 7):
         new_day_index %= 7
      new_day = days[new_day_index]

   result = f"{new_hour}:{new_minute:0>2} {new_meridiem}"
   if (start_day):
      result += f", {new_day}"
   if (days_plus):
      if (days_plus == 1):
         result += " (next day)"
      else:
         result += f" ({days_plus} days later)"
   return result
