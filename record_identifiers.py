from time import sleep as sl
import bib
print('Analysis...')
with open('C:\\Users\\Admin\\Desktop\\data.txt') as f:
  for line in f:
    line = line[:-1:]
    
    iden, week_day, month_week, summ, part_of_the_balance, hour_minute  = line.split(',')
    
    week_day = int(week_day)
    month_week = int(month_week)
    part_of_the_balance = float(part_of_the_balance)
    hour, minute = hour_minute.split(':')
    
    res = 0
  
    res = bib.month_week(month_week, res)
    res =  bib.week_day(week_day, res)
    res = bib.part_of_the_balance(part_of_the_balance, res)
    res = bib.hour(hour, res)
    res = bib.summ(summ, res)
  
    week_day = str(week_day)
    month_week = str(month_week)
    summ = str(summ)
    part_of_the_balance = str(part_of_the_balance)
    hour = str(hour)
    minute = str(minute)
  
    res = float(res)
    res = round(res, 2)
    
    result = ''
    if res >= 0.8:
      result = '+'
    else:
      result = '-'
      
    res = str(res)
    
    s = iden + week_day + ',' + month_week + ',' + summ + ',' + part_of_the_balance + ',' + hour + ':' + minute + ',' + res + ',' + result+ '\n'
    
    if result == '+':
      file = open('C:\\Users\\Admin\\Desktop\\ids.txt', 'a')
      file.write(str(iden) + '\n')
sl(2)