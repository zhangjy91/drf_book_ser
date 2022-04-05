import base64
import json

dict = {'name':'zhangasn', 'age':18}
dict_str = json.dumps(dict)

result1 = base64.b64encode(dict_str.encode('utf-8'))
print(result1)

result2 = base64.b64decode(result1)
print(result2)