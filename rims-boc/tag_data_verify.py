__author__ = "Damon"

import psycopg2

conn = psycopg2.connect(database="rims", user="postgres", password="postgres", host="192.168.3.173", port="5432")

print("连接数据库成！！")

cur = conn.cursor()

'''
cur.execute("select count(*) from (select location_id from stat.company_statistics where company_name = any(select company_name from stat.companies where company_id = any(select company_id from stat.company_summary where (select t.id from stat.company_labels t where t.company_label_name = '规上') = any(company_label_ids )))) k where k.location_id =(select h.id from stat.admin_division h where h.name_local like '吴江%')")

rows = cur.fetchall()

print("吴江区域数据",rows[0][0])

cur.execute("select count(*) from (select location_id from stat.company_statistics where company_name = any(select company_name from stat.companies where company_id = any(select company_id from stat.company_summary where (select t.id from stat.company_labels t where t.company_label_name = '规上') = any(company_label_ids )))) k where k.location_id =(select h.id from stat.admin_division h where h.name_local like '工业园区%')")

rows = cur.fetchall()

print("工业园区区域数据",rows[0][0])

cur.execute("select count(*) from (select location_id from stat.company_statistics where company_name = any(select company_name from stat.companies where company_id = any(select company_id from stat.company_summary where (select t.id from stat.company_labels t where t.company_label_name = '规上') = any(company_label_ids )))) k where k.location_id =(select h.id from stat.admin_division h where h.name_local like '昆山%')")

rows = cur.fetchall()

print("昆山区域数据",rows[0][0])

cur.execute("select count(*) from (select location_id from stat.company_statistics where company_name = any(select company_name from stat.companies where company_id = any(select company_id from stat.company_summary where (select t.id from stat.company_labels t where t.company_label_name = '规上') = any(company_label_ids )))) k where k.location_id =(select h.id from stat.admin_division h where h.name_local like '姑苏%')")

rows = cur.fetchall()

print("姑苏区域数据",rows[0][0])
'''

#使用列表进行数据的统计
# 1.定义参数的列表
list_city = ['吴江%','常熟%','工业园区%','相城区%','吴中区%']
sql_1 = "select count(*) from (select location_id from stat.company_statistics where company_name = any(select company_name from stat.companies where company_id = any(select company_id from stat.company_summary where (select t.id from stat.company_labels t where t.company_label_name = '规上') = any(company_label_ids )))) k where k.location_id =(select h.id from stat.admin_division h where h.name_local like %s)"
for i in list_city:
    cur.execute(sql_1,i)
    rows = cur.fetchall()
    print(i,rows[0][0])




