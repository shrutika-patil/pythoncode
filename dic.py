

import json
  
# Opening JSON file
# f = open('/home/rohit/Downloads/dict.json', "r")

arr = []
for line in open('/home/rohit/Downloads/dict.json', 'r'):
	arr.append(json.loads(line))

  
# returns JSON object as 
# a dictionary
# data = json.load(f)

print(arr)
# for k in my_json_str:
#     print(k)
#     print("=======================")
  
f.close()