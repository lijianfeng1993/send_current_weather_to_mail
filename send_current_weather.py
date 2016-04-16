#!/usr/bin/env/python
# -*- coding : utf-8 -*-

import sys, urllib2, urllib, json

import smtplib , sys
from email.mime.text import MIMEText 

mail_host = "smtp.qq.com"
mail_user = "1205960475@qq.com"
mail_pass = "xxxxxxxxx" 

def send_mail(to_list,sub,content):
    me = "<"+mail_user+">"
    msg = MIMEText(content,_subtype = 'plain', _charset = 'utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False

if __name__ == '__main__':
    


    url = 'http://apis.baidu.com/heweather/pro/weather?city=wuxi'
    req = urllib2.Request(url)
    req.add_header("apikey","01186f26a6760237xxxxxxxxxxxxx")

    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        result = json.loads(content)
        a = result["HeWeather data service 3.0"][0]["basic"]["city"]
        b = result["HeWeather data service 3.0"][0]["basic"]["cnty"]
        c = result["HeWeather data service 3.0"][0]["now"]["cond"]["txt"]
        cont = a + b + c
    
        if send_mail("18800585261@139.com","update weather",cont):
            print "success"
        else:
            print "get error"
        
