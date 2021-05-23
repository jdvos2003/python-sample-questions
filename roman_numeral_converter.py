def solution(roman):
  """complete the solution by transforming the roman numeral into an integer"""
  number = 0
  previous_number = 0
  mydict = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
  
  for i in roman:
    number += mydict[i]
    if previous_number != 0:
      if mydict[previous_number] < mydict[i]:
        number -= (2*mydict[previous_number])
    previous_number = i  
  return number