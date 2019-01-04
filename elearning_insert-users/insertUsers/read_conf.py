import configparser
import os

#获取config文件

def readConf(section,key):
    config = configparser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + "\elearning-users\insertUsers" + "\\interface_msg.conf"
    config.read(path,encoding="utf-8")
    return config.get(section,key)

if __name__ == '__main__':
    print(type(readConf("INTERFACEMSG","login_url")))