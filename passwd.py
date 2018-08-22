import itertools as its


class Password(object):
    #创建一个密码类
    #纯数字
    Number = '10'
    #字母
    Charater = 'abcdefghijklmnopqrstuvwxyz'
    #数字+字母
    Mix = '1234567890abcdefghijklmnopqrstuvwxyz'
    #生成密码 返回可迭代对象  元组形式
    def passwd_product(self,type,num):
        if type == 1:
            r = its.product(self.Number,repeat=num)
        elif type == 2:
            r = its.product(self.Charater,repeat=num)
        else:
            r = its.product(self.Mix,repeat=num)
        return r


    #从文件中读取密码
    def passwd_read(self,file):
        #用于存储处理后的密码列表
        pswd = []
        #读取方式打开密码文件
        f = open(file,'r')
        #读取全部行
        context = f.readlines()
        #遍历 去掉\n 添加到pswd列表
        for line in context:
            line = line.strip('\n')
            pswd.append(line)
        #将pswd列表处理成一个可迭代对象
        pswd = iter(pswd)
        #返回可迭代对象
        return pswd


