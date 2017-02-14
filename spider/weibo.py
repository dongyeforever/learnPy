# coding: utf-8

import requests

cook = {
    "Cookie": "SINAGLOBAL=1226631242676.6946.1464946980850; wvr=6; _s_tentry=login.sina.com.cn; Apache=2349329344086.266.1486866844633; ULV=1486866845012:6:3:1:2349329344086.266.1486866844633:1486784470483; UOR=tieba.baidu.com,weibo.com,www.liaoxuefeng.com; TC-Ugrow-G0=370f21725a3b0b57d0baaf8dd6f16a18; login_sid_t=ec7186138f9f08b1aa7fad3c841fbb6d; TC-V5-G0=666db167df2946fecd1ccee47498a93b; WBStorage=02e13baf68409715|undefined; SCF=AspqF-IJSBRES_rOvIsKXHbJ4tCEkCyptHaL7ySH8aXd37by-q45RPVb-EpRrD0OzW0C86KWaDfKBhOyyGH0ZqE.; SUB=_2A251pQvUDeRxGeRJ7VIU8C3NzTmIHXVW03ocrDV8PUNbmtAKLVHBkW8mOgGE1FV_XccMJ_ZOD0LWc8fBeA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF5GSHoA-rRLEq0rrqlgEIH5JpX5KzhUgL.FozNSo5fehepSo-2dJLoI7f.dc4rwgHJdNiLUJHE; SUHB=0vJJiQyyXOjM3C; ALF=1518513924; SSOLoginState=1486977924"}
url = 'http://weibo.cn/u/1890493665'
html = requests.get(url, cookies=cook).text
print(html)


