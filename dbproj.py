#!/bin/env Python 3.5.2

import psycopg2


def get_info():

    # connect to the database
    db = psycopg2.connect(database="news")
    c = db.cursor()

    # define some queries

    query1 = '''

        select title, num from toparticles limit 3;

    '''

    query2 = '''

        select name, sum(toparticles.num) as total
        from toparticles join authors
        on toparticles.author = authors.id
        group by authors.name order by total desc;

    '''

    query3 = '''

        select * from errors where percent > 1;

    '''

    c.execute(query1)
    result = c.fetchall()
    print('The most popular articles are:\n')
    for r in result:
        print('\"' + r[0] + '\", with ' + str(r[1]) + ' views')

    c.execute(query2)
    result = c.fetchall()
    print('\n\nThe most popular authors are:\n')
    for r in result:
        print(r[0] + ', with ' + str(r[1]) + ' views')

    c.execute(query3)
    result = c.fetchall()
    print(
        '\n' + str(len(result)) +
        ' day(s) in which the percentage of errors was higher than 1%:\n')
    for r in result:
        print(str(r[0]) + ', with ' + str(r[1])+"%")

    # close the connection to the database when we're finished
    db.close

if __name__ == '__main__':
    get_info()
