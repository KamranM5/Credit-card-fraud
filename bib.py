def week_day(a, res):
  a = int(a)
  if a == 2:
    res += 0.25
    
  elif a == 3:
    res += 0.125
    
  elif a == 1 or int(a) >= 3:
    res += 0.0625
  return res

def month_week(a, res):
  a = int(a)
  if a == 1 or a == 4:
    res += 0.25
    
  elif a == 2 or a == 3:
    res += 0.125
    
  else:
    res += 0.0675
  return res

def part_of_the_balance(a, res):
  a = float(a)
  if a >= 0.8:
    res += 0.25
    
  elif a >= 0.5:
    res += 0.125
    
  else:
    res += 0.0625
  return res

def hour(a, res):
  a = int(a)
  if 11 <= a <= 14:
    res += 0.25
    
  elif (7 <= res < 11) and (14 < a <= 20):
    res += 0.125
    
  else:
    res += 0.0625
  
  return res

def summ(a, res):
  a = int(a)
  if a % 1000 == 0:
    res += 0.25
  elif (a % 100 == 0) and (a % 1000 != 0):
    res += 0.125
  else:
    res += 0.0625
  return res