def fibonnacci(n):
  index = 1 
  x = 1
  y = 1
  while index < n:
    y = x + y
    x = y - x
    index = index + 1
  return y
   
print(fibonnacci(5))  
