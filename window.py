import passwd
import wifi
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox



class Window(object):
    #主窗口
    def __init__(self):
        self.base = tk.Tk()
        self.base.geometry('400x220+550+300')
        self.base.resizable(0,0)
        self.base.title('飞羽WiFi爆破')




        #按钮
        #文件导入
        def fileloads():
            #文件选择  txt文件
            s = filedialog.askopenfilename(title='选择字典',filetypes=[('Text file','*.txt')])
            fileroad.set(s)

        self.fileButton = tk.Button(self.base,text='文件导入',command=fileloads)

        #连接
        def connect():
            index = self.wifiList.curselection()
            try:
                wifiname = self.wifiList.get(index)
            except:
                messagebox.showwarning(title='警告', message='请选择一个WiFi!!!')
            else:
                connectWindow = tk.Tk()
                connectWindow.title('连接')
                connectWindow.resizable(0, 0)
                connectWindow.geometry('150x60+700+350')

                passwordLable = tk.Label(connectWindow,text='密码：')
                passwordEntry = tk.Entry(connectWindow,width=15)

                def connect():
                    password = passwordEntry.get()
                    #connectwifi = wifi.WiFi()
                    state = wifi.WiFi().normalconnect(name=wifiname,password=password)
                    if state:
                        messagebox.showinfo(message='连接成功！！！')
                    else:
                        messagebox.showerror(message='密码错误！！！')
                    connectWindow.destroy()
                sub = tk.Button(connectWindow,text=' 连 接 ',command=connect)

                passwordLable.place(x=10,y=10,anchor='nw')
                passwordEntry.place(x=45,y=10,anchor='nw')
                sub.place(x=100,y=30)

                connectWindow.mainloop()


        self.connectButton = tk.Button(self.base,text='连\n接',command=connect)
        #断开连接

        def disconnect():
            if wifi.WiFi().wifi_disconnect():
                messagebox.showinfo(message='成功断开连接！！！')



        self.disconnectButton = tk.Button(self.base,text='断\n开\n连\n接',command=disconnect)


        #输入框
        threadnum = tk.IntVar()
        digitnum = tk.IntVar()
        self.thread_num_Entry = tk.Entry(self.base,width=6,textvariable=threadnum)
        self.passwd_digit_Entry = tk.Entry(self.base,width=6,textvariable=digitnum)

        #线程爆破
        def threadblase():
            threadNum = self.thread_num_Entry.get()
            digitNum = self.passwd_digit_Entry.get()
            index = self.wifiList.curselection()
            try:
                wifiname = self.wifiList.get(index)
            except:
                messagebox.showwarning(title='警告', message='请选择一个WiFi！！！')
            else:
                try:
                    threadnum = int(threadNum)
                    digitnum = int(digitNum)
                except:
                    messagebox.showerror(message='输入含有非数字内容')
                else:
                    if threadnum > 4500 or threadnum < 1:
                        messagebox.showwarning(message='线程数应该在（0-4500）之间')
                    elif digitnum > 11 or digitnum < 1:
                        messagebox.showwarning(message='请输入正确的密码位数\n目前支持最大密码11位')
                    else:
                        try:
                            pswd = int(way.get())
                            iterPassword = passwd.Password().passwd_product(type=pswd,num=int(digitNum))
                        except:
                            messagebox.showwarning(message='请选择密码类型！！！')
                        else:
                            request = messagebox.askokcancel(message='该过程可能会非常漫长并且可能会占用系统资源，确定是否继续？')
                            if request:
                                messagebox.showinfo(message='请等待...')
                                try:
                                    result = wifi.WiFi().thread_connect(threadnum=threadNum,name=wifiname,password=iterPassword)
                                except:
                                    pass
                                finally:
                                    if result == None :

                                        messagebox.showinfo(message='爆破失败！！！')
                                    else:
                                        messagebox.showinfo(message='爆破成功  密码：'+str(result[0]))
                            else:
                                pass
        self.threadblaseButton = tk.Button(self.base,text='开始爆破',command=threadblase)




        #文件爆破
        def fileblase():
            loads = fileroad.get()
            index = self.wifiList.curselection()
            try:
                wifiname = self.wifiList.get(index)
            except:
                messagebox.showwarning(title='警告', message='请选择一个WiFi！！！')
            else:
                try:
                    password = passwd.Password().passwd_read(file=loads)
                except:
                    messagebox.showerror(message='请导入文件！！！')
                else:
                    result = wifi.WiFi().blastconnect(name=wifiname,password=password)
                    if result == -1:
                        messagebox.showinfo(message='爆破失败')
                    else:
                        messagebox.showinfo(message='爆破成功  密码为：'+result)



        self.fileblaseButton = tk.Button(self.base, text='开始爆破', command=fileblase)





        #扫描
        def scan():
            wifilist = wifi.WiFi().wifi_scan()
            self.wifiList.delete(0,'end')
            for i in wifilist:
                self.wifiList.insert(0,i)

        self.scanButton = tk.Button(self.base,text='扫\n描',command=scan)




        #选择按钮
        option = tk.IntVar()

        def select():
            if option.get() == 1:
                self.threadblaseButton.config(state='disabled')
                self.thread_num_Entry.config(state='disabled')
                self.fileButton.config(state='normal')
                self.fileblaseButton.config(state='normal')
                self.passwd_digit_Entry.config(state='disabled')
                self.numRadio.config(state='disabled')
                self.charRadio.config(state='disabled')
                self.mixRadio.config(state='disabled')

            else:
                self.fileButton.config(state='disabled')
                self.thread_num_Entry.config(state='normal')
                self.fileblaseButton.config(state='disabled')
                self.threadblaseButton.config(state='normal')
                self.passwd_digit_Entry.config(state='normal')
                self.numRadio.config(state='normal')
                self.charRadio.config(state='normal')
                self.mixRadio.config(state='normal')

        #文件爆破
        self.fileRadio = tk.Radiobutton(self.base,text='文件爆破',value=1,variable=option,command=select)
        #线程爆破
        self.threadRadio = tk.Radiobutton(self.base,text='线程爆破',value=2,variable=option,command=select)

        def test():
            pass
        way = tk.IntVar()
        self.numRadio = tk.Radiobutton(self.base,text='纯数字',value=1,variable=way)
        self.charRadio = tk.Radiobutton(self.base,text='纯字母',value=2,variable=way)
        self.mixRadio = tk.Radiobutton(self.base,text='数字字母',value=3,variable=way)



        #列表
        self.wifiList = tk.Listbox(self.base,selectmode='BROWSE')#鼠标浏览模式
        self.wifiList.yview_scroll(number=10,what='units')
        self.wifiList.select_clear(0,1)#取消默认选中

        #标签
        fileroad = tk.StringVar()
        self.fileLable = tk.Label(self.base,bg='#fff',width=28,textvariable=fileroad)
        self.threadLable = tk.Label(self.base,width=8,text='线程个数：')
        self.digitLable = tk.Label(self.base,width=8,text='密码位数：')

        self.lineLable = tk.Label(self.base,text='\n\n\n\n\n\n\n\n\n\n\n', bg='#F5DEB3')

        self.introductLable1 = tk.Label(self.base,width=60,bg='#90EE90',text='欢迎使用飞羽WiFi爆破（测试版）！！！')
        self.introductLable2 = tk.Label(self.base,width=60,bg='#90EE90',text='1.支持最大线程4500（线程过多可能造成卡顿）2.密码最大支持11位')





    def disable(self):
        # 禁用控件
        self.threadblaseButton.config(state='disabled')
        self.thread_num_Entry.config(state='disabled')
        self.fileblaseButton.config(state='disabled')
        self.fileButton.config(state='disabled')
        self.passwd_digit_Entry.config(state='disabled')
        self.numRadio.config(state='disabled')
        self.charRadio.config(state='disabled')
        self.mixRadio.config(state='disabled')

    def arragement(self):
        #控件部署
        #按钮部署
        self.fileButton.place(x=200,y=50,anchor='nw')
        self.connectButton.place(x=133,y=76,anchor='nw')
        self.disconnectButton.place(x=133, y=120, anchor='nw')
        self.threadblaseButton.place(x=320, y=170, anchor='nw')
        self.scanButton.place(x=133, y=32, anchor='nw')
        self.fileblaseButton.place(x=270,y=50,anchor='nw')

        #选择按钮部署
        self.fileRadio.place(x=200,y=20,anchor='nw')
        self.threadRadio.place(x=200,y=105,anchor='nw')

        self.numRadio.place(x=320,y=110)
        self.charRadio.place(x=320,y=130)
        self.mixRadio.place(x=320,y=150)


        #列表部署
        self.wifiList.place(x=10,y=30,anchor='nw')

        #标签部署
        self.fileLable.place(x=200,y=80,anchor='nw')
        self.threadLable.place(x=200,y=130,anchor='nw')
        self.digitLable.place(x=200,y=155,anchor='nw')

        self.introductLable1.place(x=0,y=0,anchor='nw')
        self.introductLable2.place(x=0,y=200,anchor='nw')

        self.lineLable.place(x=190,y=20,anchor='nw')


        #输入框部署
        self.thread_num_Entry.place(x=255,y=130,anchor='nw')
        self.passwd_digit_Entry.place(x=255,y=155,anchor='nw')


    def run(self):
        #运行
        self.disable()
        self.arragement()
        self.base.mainloop()



if __name__ == '__main__':
    feiyu = Window()
    feiyu.run()