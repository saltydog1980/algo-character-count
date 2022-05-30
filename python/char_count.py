import re
from functools import cmp_to_key

def char_count(string):
#dictionary to log characters and count
  char_dict = {}
  #took string to lowercase, removed anything not a alpha and cast to a list
  base_list = list(re.sub("[^a-z]+", '', string.lower()))
  #looping through the base list and if already in dict +1, else setting it to 1
  for char in base_list:
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1
  #taking dict items and using map to dump the key value pairs into a 2D list
  count_list = list(map(list, char_dict.items()))
  
  #defining a compare function to call with sort method later
  def compare(a, b):
      #if count matches then sort by alpha in ascending order
      if a[1] == b[1]: 
        return 1 if a[0] > b[0] else -1
      #else sort by count in descending order
      else:
        return 1 if a[1] < b[1] else -1
  #calling sort method against my countlist and using my compare function defined above
  count_list.sort(key=cmp_to_key(compare))
  #returning the sorted 2D countlist 
  return count_list
