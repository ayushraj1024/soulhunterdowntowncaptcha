import json
x = 1
y = 2
sum = x+y

a = {"sum":sum};

python2json = json.dumps(a)
print(python2json)