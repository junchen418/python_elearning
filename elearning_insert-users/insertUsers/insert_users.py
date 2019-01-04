import requests

'''配置文件中读取参数'''
login_msg = read_conf.readConf("INTERFACEMSG","login_msg")
login_url = read_conf.readConf("INTERFACEMSG","login_url")
insert_user_url = read_conf.readConf("INTERFACEMSG","insert_user_url")
emails_url =read_conf.readConf("INTERFACEMSG","emails_url")

'''添加用户user_id'''
#仅需要告知用户的user_id，即可进行批量添加用户进行课程的学习

list_params = ['10221']




'''声明全局变量'''
global null
null = ''

'''登录'''
response_login = requests.post(login_url,json=eval(login_msg))
print(response_login.status_code)

'''提取authentication'''
jwt_token = response_login
jwt_token1 = jwt_token.json()['jwt']
token = jwt_token.json()['api_path']
token = token.replace("\\", "")
tokens = (eval(token)['path'])

'''提取api_token'''
api_token = tokens['POSTinno-course/elearn/enroll_users/{packageId}']['token']
headers = {'Authorization':jwt_token1,'X-API-Token':api_token,'Content-Type':'application/json'}
response_insert_users = requests.post(insert_user_url,json = list_params, headers=headers)
print(response_insert_users.status_code)

'''是否触发邮件通知'''
api_token1 = tokens['PUTinno-course/elearn/enroll_users/{packageId}/sendemail_status']['token']
headers1 = {'Authorization':jwt_token1,'X-API-Token':api_token1}
response_emails = requests.put(emails_url,headers=headers1)
print(response_emails.text)

