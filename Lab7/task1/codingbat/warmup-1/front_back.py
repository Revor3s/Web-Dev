def front_back(str):
  if len(str)<=1:
    return str
  first=str[len(str)-1]
  last=str[0]
  mid=str[1:len(str)-1]
  return first+mid+last