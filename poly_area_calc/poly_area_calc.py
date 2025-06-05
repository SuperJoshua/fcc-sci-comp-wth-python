class Rectangle:
   def __init__(self, width, height):
      self.width = width
      self.height = height
   
   def __repr__(self):
      return f"Rectangle(width={self.width}, height={self.height})"

   def get_area(self):
      return self.width * self.height

   def get_diagonal(self):
      return (self.width**2 + self.height**2)**0.5

   def get_amount_inside(self, rect):
      n_wide = self.width // rect.width
      n_high = self.height // rect.height
      if n_wide > 0 and n_high > 0:
         return n_wide * n_high
      return 0

   def get_perimeter(self):
      return 2 * self.width + 2 * self.height
   
   def get_picture(self):
      if self.width > 50 or self.height > 50:
         return "Too big for picture."
      shape = ['*' * int(self.width) for row in range(int(self.height))]
      s = ''
      for row in shape:
         s += f"{row}\n"
      return s
   
   def set_height(self, height):
      self.height = height
   
   def set_width(self, width):
      self.width = width

class Square(Rectangle):
   def __init__(self, side):
      super().__init__(side, side)
   
   def __repr__(self):
      return f"Square(side={self.width})"

   def set_height(self, side):
      self.set_side(side)

   def set_side(self, side):
      super().set_width(side)
      super().set_height(side)

   def set_width(self, side):
      self.set_side(side)
