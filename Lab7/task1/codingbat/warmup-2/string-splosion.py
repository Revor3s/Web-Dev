def string_splosion(str):
  result = ''
  for n in range(0,len(str)+1):
    result += str[:n]
  return result