class Rectangle:
  def __init__(self,width,height):
    self.width=width
    self.height=height
  def set_width(self,new_width):
    self.width=new_width
  def set_height(self,new_height):
    self.height=new_height
  def get_area(self):
    return self.width*self.height
  def get_height(self):
    return self.height
  def get_width(self):
    return self.width

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  def get_picture(self):
    res=[]
    if self.width<50 and self.height<5:
      for i in range(self.height):
        res.append(('*'*self.width)+"\n")
      return ''.join(res)
    else:
      return "Too big for picture."
  def __str__(self):
      return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"

  def get_amount_inside(self,shape):
    ht=int(self.get_height()/shape.get_height())
    wd=int(self.get_width()/shape.get_width())
    if ht!=0 and wd!=0:
      return int(ht)*int(wd)
    else:
      return 0# 8 6 width 15 5
  
class Square(Rectangle):
  def __init__(self,side):
    super().__init__(side,side)
  def set_side(self,new_side):
    super().set_width(new_side)
    super().set_height(new_side)
  def __str__(self):
    return "Square(side="+str(self.width)+")"
  def set_width(self,new_side):
    super().set_width(new_side)
    super().set_height(new_side)
  def set_height(self,new_side):
    super().set_width(new_side)
    super().set_height(new_side)


