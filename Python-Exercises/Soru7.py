
class Shape:

   # constructor
   def __init__(self, initx, inity):
      self.moveTo(initx, inity)

   # accessors for x & y
   def getX(self):
      return self.x
   def getY(self):
      return self.y
   def setX(self, newx):
      self.x = newx
   def setY(self, newy):
      self.y = newy

   # move the shape position
   def moveTo(self, newx, newy):
      self.setX(newx)
      self.setY(newy)
   def rMoveTo(self, deltax, deltay):
      self.moveTo(self.getX() + deltax, self.getY() + deltay)

   # abstract draw method
   def draw(self):
      pass
    
   

