class Category:
   def __init__(self, category):
      self.category = category
      self.ledger = []
   
   def __repr__(self):
      info = f"{self.category:*^30}\n"
      for item in self.ledger:
         info += f"{item['description'][:23]: <23}{item['amount']: >7.2f}\n"
      info += f"Total: {self.get_balance()}"
      return info

   def check_funds(self, amount):
      if (self.get_balance() - amount >= 0):
         return True
      return False

   def deposit(self, amount, description = ''):
      self.ledger.append({'amount': amount, 'description': description})

   def get_balance(self):
      return sum([obj['amount'] for obj in self.ledger])

   def transfer(self, amount, category):
      if (self.withdraw(amount, f"Transfer to {category.category}")):
         category.deposit(amount, f"Transfer from {self.category}")
         return True
      return False

   def withdraw(self, amount, description = ''):
      if (self.check_funds(amount)):
         self.deposit(-amount, description)
         return True
      return False


def create_spend_chart(categories):
   # This is a mess...
   bar_chart = "Percentage spent by category\n"

   cats = [cat.category for cat in categories]
   longest_cat = max([len(cat) for cat in cats])
   cats = [f"{cat: <{longest_cat}}" for cat in cats]

   bar = "   " + "---" * len(cats) + '-\n'

   withdrawels = []
   for cat in categories:
      withdrawels.append(sum([obj['amount'] for obj in cat.ledger if obj['amount'] < 0] ))
   total_withdrawels = sum(withdrawels)
   percents = ["o" * (int(w / total_withdrawels * 10) + 1) for w in withdrawels]
   percents = [f"{perc: >11}" for perc in percents]

   y_axis = list(range(100, -1, -10))
   y_axis = [f"{y: >3}" for y in y_axis]

   for i in range(11):
      bar_chart += f"{y_axis[i]}|"
      for perc in percents:
         bar_chart += f" {perc[i]} "
      bar_chart += " \n"

   bar_chart += bar

   for i in range(longest_cat):
      bar_chart += "   "
      for cat in cats:
         bar_chart += f" {cat[i]} "
      bar_chart += " \n"

   return bar_chart[:-1]
