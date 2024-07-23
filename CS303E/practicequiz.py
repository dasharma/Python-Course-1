def removeNegatives(lst):
  if lst == []:
    return lst
  elif lst[0] > 0:
    return [lst[0]] + removeNegatives(lst[1: ])
  else:
    return removeNegatives(lst[1:])
