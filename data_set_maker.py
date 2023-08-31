from random import randint as r
print('Dataset making...')
for i in range(9999):
  iden = str(int(r(0, 100000000)))
  
  week_day = str( int( r(1, 7) ) )
  month_week = str(int ( r(1, 4) ) )
  summ = str(int ( r(1, 1000000) ) )
  part_of_the_balance = str( float ( r(0, 100) / 100) )
  hour = str (int ( r(0, 24) ) )
  minute = str (int ( r(0, 60) ) )
  
  res = 0

  text = open('data.txt', 'a')
  
  wr = iden + ',' + week_day + ',' + month_week + ',' + summ + ',' + part_of_the_balance + ',' + hour + ':' + minute + '\n'
  text.write(wr)
print('Done')
