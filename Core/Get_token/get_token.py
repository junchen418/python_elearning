__author__ = "Damon_xuchen"

import requests
url = "http://qa-dev-center.zhihuiya.com/developer/api/bundles?clientId=9a5090de106f4f00a277cb7999e433e0"
headers = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiJ9.eyJ0ZW5hbnRfaWQiOiJkNmY0ODRkNjk1YTZjYWIxYjJlMzY1YzRkNWEzMzg1YiIsInN1YiI6IjYwYWIzNzE2NmEwNjQzYjA5ZWQ2YmEzMjBhYTMxZjVhIiwic2Vzc2lvbiI6ImRhYWFlNTI3N2NlYTQyMzQ4ODU5MWI0ZTk2OTg5MjhjIiwiaXNzIjoicGF0c25hcCIsImV4cCI6MTU0ODIzOTgxMiwiaWF0IjoxNTQ4MjM4MDEyLCJqdGkiOiI1MzMwODMzOC03YmY5LTQzYTUtYTIyNi02ZDIwMmRmYzFkZmIiLCJjbGllbnRfaWQiOiIxMCIsImF1dGhvcml0aWVzIjpbIjEwIiwiMTZkYzQ4YjY5OTUzNGQ4NGI5YTgxMmMyZWQwZTA3M2QiLCIyODkyZTFhNGI5NWE0Yjg1OWNiMGRkOWY5ODQyYzZiOCIsIjgwNTZjMjgzYzRiYjQ4YTA4NmYxY2UwMzYxNmZhMDk4IiwiYmFja29mZmljZS1hZG1pbiIsImJhY2tvZmZpY2UtZGV2ZWxvcGVyIiwiYmQzMTc0ZDNjMWEzNDYzMWExNzQyZjY2MjEyZGU2MjkiLCJjb3Vyc2VfY3VzdG9tX3Bhc3Nwb3J0XzllOTY4YTkyMGIyYWQ1NDFiODVkMzVmNmQ3N2FkMzNmIiwiY291cnNlX3B1YmxpY19kYWNiYmExMmZhZmMxZDI2NWZiOWZlMWE1Nzc0ZGY5NCIsImNvdXJzZV9zdXBlcl92aXBfYTRmZGU1MTAxODg3NTZjZWI0OGJiODhiNjVhOWM0YmQiLCJmMWFjYmNiZGY1Y2U0NjYwOTQ2OTI1YzIzZGY4YTQ5MSIsImZmZTYwZjMxMjU2NWNhZWQzMjM4MzI0YTk0MjdmZWNkIl19.pNjvLOT0qehSlSqCN7UZ-XoPk2KOzZkHJMwSYEVyhWt-fcYxGFzkRp5xGJALk4vdjm0R8jHWwyv9nPm-zDf5MpEmwp1K9XwlhqNprFSa9uRLvNpRPzYiDszZA38MYD0klBpLx38gymUMQD1Z01hiSm5KR_qRXCd0luXhlPGIfNc"
}
response = requests.request("GET", url, headers=headers)
print(response.json())
