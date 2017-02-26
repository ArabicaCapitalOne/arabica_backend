import urllib, json

with open("out.json") as data_file:
    data = json.load(data_file)

dic = {}
f = open("data.csv", "w")
for item in data:
    date = str(item[u'purchase_date']).split('-')
    newdate = date[1] + date[0]
    amount = float(item[u'amount'])
    if newdate in dic:
        dic[newdate] = dic[newdate] + amount
    else:
        dic[newdate] = 0
for key, val in dic.iteritems():
    f.write(key + ',' + str(val) + '\n')
f.close()
