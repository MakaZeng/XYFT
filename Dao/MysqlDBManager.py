import MySQLdb
import MysqlDBConfig as DBC


def maka_do_sql(sql):
    try:
        print sql
        conn = MySQLdb.connect(host=DBC.Host, user=DBC.Name, passwd=DBC.Password, port=DBC.Port, charset='utf8')
        cur = conn.cursor()
        conn.select_db(DBC.Database)

        result = cur.execute(sql)

        conn.commit()
        cur.close()
        conn.close()

        return result
    except MySQLdb.Error, e:
        print "maka_do_sql mysql Error %d: %s" % (e.args[0], e.args[1])