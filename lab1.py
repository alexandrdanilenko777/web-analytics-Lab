import re
import json
from urllib import urlopen
#from geoip import geoip

f = open("/Users/Alexandr/Downloads/Study/tkach/access.log","r")
rf = f.read()


#unique users (count)

def daily_u(readf):
    day = re.findall(r'\d{1,2}/\w{1,3}/\d{1,4}',readf)
    s = set(day)
    d = list(s)
    i=0
    print ("Daily users number:")
    for i in range(len(d)):
        cmp = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - - \[" + d[i]
        cm = re.compile(cmp)
        ip = cm.findall(rf)
        print ("{}:{}".format(d[i],len(set(ip))))
        i=i+1

#Range by user-agents

def get_useragent_full(readf):
    agent = re.findall(r'" ".+',rf)
    s1 = set(agent)
    a = list(s1)
    j=0
    #temp = 0
    print ("User agent number:")
    for j in range(len(a)):
        print ("{}:{}".format(a[j],agent.count(a[j])))
        #temp = temp + agent.count(a[j])
        j=j+1

#Range by os

def os_range(readf):
    os = re.findall(r'\([^Kc"ias_crawler"].*?;',readf)
    s2 = set(os)
    o = list(s2)
    k = 0
    sum = 0
    for k in range(len(o)):
        sum=sum+os.count(o[k])
    k = 0
    for k in range(len(o)):
        os_pr = o[k]
        per = round(((os.count(o[k])*100)/sum),2)
        print ("{}:{}%".format(os_pr[1:],per))


#country

#r = geoip.GeoIp()
#r.load_memory()
#pr = r.resolve("78.46.24.99").country_code
#print (pr)



#bots detected
def bots(readf):
    agent = re.findall(r'" ".+',readf)
    s1 = set(agent)
    a = list(s1)
    j=0
    b_n=0
    for j in range(len(a)):
        a_l = a[j].lower()
        is_bot = a_l.find("bot")
        if is_bot>-1:
            b_n=b_n+1
        j=j+1
    print ("{} unique bots detected".format(b_n))


daily_u(rf)
get_useragent_full(rf)
os_range(rf)
#country_range
bots(rf)

f.close()


