##Adam and Eve

class Human:
  def __init__(self,sex,name):
    self.sex=sex
    self.name=name
class Man(Human):
  def __init__(self,name):
    Human.__init__(self,'Man',name)
class Woman(Human):
  def __init__(self,name):
    Human.__init__(self,'Woman',name)  

def God():
  Man1 = Man('Adam')
  Woman1 = Woman('Eva')
  return Man1, Woman1