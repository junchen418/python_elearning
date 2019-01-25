__author__ = "Damon"
import psycopg2

conn = psycopg2.connect(database="rims", user="postgres", password="postgres", host="192.168.3.173", port="5432")

print("连接数据库成！！")

cur = conn.cursor()

# cur.execute('select * from /"admin_division/"')

# query_city = [('张家港%',)]

# print(type(query_city[0]))

# sql = "select count(*) from stat.company_statistics t where t.location_id =(select h.id from stat.admin_division h where h.name_local like %s)"
#
# cur.executemany(sql,query_city)

# cur.execute("select count(*) from stat.company_statistics t where t.location_id =(select h.id from stat.admin_division h where h.name_local like '张家港%')")

# rows = cur.fetchall()
#
# print('张家港市企业分布数量',rows[0][0])

# cur.execute("select count(*) from stat.company_statistics t where t.location_id =(select h.id from stat.admin_division h where h.name_local like '姑苏区%')")

# rows = cur.fetchall()
#
# print('姑苏区企业分布数量',rows[0][0])
#
# cur.execute("select count(*) from stat.company_statistics t where t.location_id =(select h.id from stat.admin_division h where h.name_local like '昆山市%')")
#
# rows = cur.fetchall()
#
# print('昆山市企业分布数量',rows[0][0])




