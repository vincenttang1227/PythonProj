import requests
import pandas as pd
from io import StringIO

def conver2digit(x):
    if x < 10 :
        return '0' + str(x)
    else:
        return str(x)
    
inputDate = input().split(' ')

syear = int( inputDate[0] )
smonth = int( inputDate[1] )
sday = int( inputDate[2] )
dateString = str(syear) + conver2digit(smonth) + conver2digit(sday)

res = requests.get("http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date="+dateString+"&type=ALLBUT0999&_=1544167266618")
#print( res.text[:1000] )

file1 = open('stock.csv', 'w', encoding='utf-8-sig')
file1.write( res.text )
file1.close()

newlines = []
content = res.text.split('\r\n')
for i in range( len(content) ):
    if len(content[i].split('","')) == 16:
        newlines.append( content[i] )
#print( newlines[:10] )
df = pd.read_csv(StringIO("\r\n".join(newlines).replace('=','')))
df = df.set_index('證券代號')
#print( df.head() )
df = df.astype( str )
#print( df.dtypes )
df = df.apply( lambda s: s.str.replace("," , "") )
df = df.apply( lambda s: pd.to_numeric(s, errors="coerce") )
df = df[ df.columns[ df.isnull().sum() != len(df) ] ]
#print( df[ df['收盤價']/df['開盤價']>1.05 ] )
#print( df.head() )

df.to_csv(dateString + ".csv",encoding="utf-8-sig")

df1 = pd.read_csv(dateString + ".csv",encoding="utf-8-sig",index_col=['證券代號'])
#print( df1.head() )

import sqlite3

conn = sqlite3.connect("stock.sqlite3")

df.to_sql("d"+dateString, conn, if_exists="replace")
df2 = pd.read_sql("select * from d"+dateString,conn, index_col=['證券代號'])
print( df2.head() )



