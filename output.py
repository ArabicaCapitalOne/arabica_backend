import urllib, json

with open("out.json") as data_file:
    data = json.load(data_file)

dic = {}
f = open("data.csv", "w")
for item in data:
    date = str(item[u'purchase_date']).split('-')
    newdate = (int(date[0])-2010) * 12 + int(date[1])
    amount = float(item[u'amount'])
    if newdate in dic:
        dic[newdate] = dic[newdate] + amount
    else:
        dic[newdate] = 0
f.write('month,amount\n')
for key, val in dic.iteritems():
    f.write(str(key) + ',' + str(val) + '\n')
f.close()
