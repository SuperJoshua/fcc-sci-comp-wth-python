def arithmetic_arranger(problems, show_answers = False):
   padding_w = 4
   padding = ' ' * padding_w
   top_row = ''
   bottom_row = ''
   bar_row = ''
   solution_row = ''

   if (len(problems) > 5):
      return "Error: Too many problems."
   for string in problems:
      a, o, b = string.split()

      if o not in "+-":
         return "Error: Operator must be '+' or '-'."
      
      a_w = len(a)
      b_w = len(b)
      if a_w > 4 or b_w > 4:
         return "Error: Numbers cannot be more than four digits."
      
      try:
         a_n = int(a)
         b_n = int(b)
      except ValueError:
         return "Error: Numbers must only contain digits."
      
      bar_w = 2 + max([a_w, b_w])
      bar = '-' * bar_w
      bar_row += bar + padding
      
      top_row += f"{a: >{bar_w}}{padding}"
      bottom_row += f"{o}{b: >{bar_w - 1}}{padding}"

      solution = ''
      if o == '+':
         solution = str(sum([a_n, b_n]))
      else:
         solution = str(sum([a_n, -b_n]))
      solution_row += f"{solution: >{bar_w}}{padding}"
   
   top_row = top_row[:-padding_w] + '\n'
   bottom_row = bottom_row[:-padding_w] + '\n'
   bar_row = bar_row[:-padding_w]
   solution_row = solution_row[:-padding_w]
   result = top_row + bottom_row + bar_row
   if show_answers:
      result += '\n' + solution_row
   return result
