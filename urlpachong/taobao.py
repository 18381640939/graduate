# -*- coding: utf-8 -*-
import requests
import re
import cgi,cgitb
import MySQLdb
#获取页面、
def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		print("")
#对页面进行解析
def parsePage(ilt,html):
	try:
		#查找价格
		plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		#查找物品
		tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
		for i in range(len(plt)):
			price=eval(plt[i].split(':')[1])
			title=eval(tlt[i].split(':')[1])
			ilt.append([price,title])
	except:
		print("")
#进行打印
def printGoodsList(ilt):
	tplt = "{:4}\t{:8}\t{:16}"
	print(tplt.format("id", "price", "name"))
	count = 0
	for g in ilt:
		count = count + 1
		print(tplt.format(count, g[0], g[1]))


#数据库写入
def printgoods(ilt):
    tplt = "{:2}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    conn = MySQLdb.connect("localhost","root","123456","graduate",charset="utf8")
    cur = conn.cursor()
    sqlc = '''create table goods(
              id int(11) not null auto_increment primary key,
              price float not null,
              name varchar(255) not null)DEFAULT CHARSET=utf8;'''
    try:
        A = cur.execute(sqlc)
        conn.commit()
        print('成功')
    except:
        print("错误")
    for g in ilt:
        count = count + 1
        b=tplt.format(count, g[0], g[1])

        sqla = '''insert into  goods(name,price)
        		  values(%s,%s);'''
        try:
            B = cur.execute(sqla,(g[1],g[0]))
            conn.commit()
            print('成功')
        except:
            print("错误")
    conn.commit()
    cur.close()
    conn.close()

def main():
	# form=cgi.FieldStorage()
	goods="物联网"
	depth=2
	start_url='https://s.taobao.com/search?q='+goods
	infoList=[]
	for i in range(depth):
		try:
			#内容转换为字符串
			url=start_url+'&s='+str(44*i)
			html=getHTMLText(url)
			parsePage(infoList , html)
		except:
			continue

	printGoodsList(infoList)

main()
