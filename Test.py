#!/usr/bin/env python
import psycopg2


def solve1():
    conn = psycopg2.connect(dbname="news")
    cur = conn.cursor()
    cur.execute("""select articles.title, count(*) as num from articles,
     log where log.path like concat('/article/',articles.slug)
      group by articles.title order by num desc limit 3;""")
    items = cur.fetchall()
    conn.close()
    for item in items:
        print "The most popular three articles of all time :"
        print'%s - %d views' % (item[0], item[1])


def solve2():
    conn = psycopg2.connect(dbname="news")
    cur = conn.cursor()
    cur.execute("""select authors.name, count(*) as num from articles,
     log, authors where log.path like concat('/article/',articles.slug)
     and articles.author = authors.id group by authors.name order by
     num desc;""")
    items = cur.fetchall()
    conn.close()
    for item in items:
        print "The most popular article authors of all time:"
        print '%s - %d views' % (item[0], item[1])


def solve3():
    conn = psycopg2.connect(dbname="news")
    cur = conn.cursor()
    cur.execute("""select time::DATE,round(((Ecount::decimal/num)*100),2) as percentage
     from(
     select log.time::DATE ,count(*) num,
     sum(case when status != '200 OK' then 1 else 0 end)
     Ecount from log  group by log.time::DATE ) as er
      where Ecount>(num/100);""")
    items = cur.fetchall()
    conn.close()
    for item in items:
        print "days had more than 1% of requests lead to errors :"
        print str(item[0])+" - "+str(item[1])+"%errors"

if __name__ == '__main__':
    print("please enter which answer of the three question you want?!")
    a = input()
    if a == 1:
        print("your choise is 1")
        solve1()
    elif a == 2:
        print("your choise is 2")
        solve2()
    elif a == 3:
        print("your choise is 3")
        solve3()
    else:
        print("invalid input")
