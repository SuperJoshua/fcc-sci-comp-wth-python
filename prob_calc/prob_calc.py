import copy
import random

class Hat:
   def __init__(self, **keywords):
      self.contents = []
      for key, value in keywords.items():
         for n in range(value):
            self.contents.append(key)
   
   ''' I had to redesign this since the test was apparently expecting me to use random.choice. This is the old solution, and I don't see what would otherwise be wrong with it.

   def draw(self, n):
      random.shuffle(self.contents)
      if n > len(self.contents):
         random_group = self.contents[:]
         self.contents = []
         return random_group
      random_group = self.contents[:n]
      self.contents = self.contents[n:]
      return random_group '''
   
   def draw(self, n):
      random_group = []
      if n > len(self.contents):
         random_group = self.contents[:]
         self.contents = []
         return random_group
      for i in range(n):
         ball = random.choice(self.contents)
         random_group.append(ball)
         self.contents.remove(ball)
      return random_group


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
   M = 0
   N = num_experiments
   for _ in range(N):
      h = copy.deepcopy(hat)
      random_group = h.draw(num_balls_drawn)
      actual_balls = {}
      for ball in random_group:
         if ball in actual_balls:
            actual_balls[ball] += 1
         else:
            actual_balls[ball] = 1
      passing = True
      for ball in list(expected_balls):
         if ball not in actual_balls or expected_balls[ball] > actual_balls[ball]:
            passing = False
            break
      if passing:
         M += 1
   return M / N
