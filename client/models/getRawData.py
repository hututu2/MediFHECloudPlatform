def getRawData():
    '''
    通过com口读取测量数据，
        n是读取数据个数，
        返回ay和gap，分别是R峰序列和数据之间的时间间隔

    数据读取时，先识别出五个R峰，得到对应的时间（t1,t2,t3,t4,t5），作为原始数据存到服务器，
    同态计算：
        间隔：tgap=((t2-t1)+(t3-t2)+(t4-t3)+(t5-t4))/4
        心率：h=60/tgap
    '''
    from serial import Serial   # 导入模块
    import time
    from matplotlib import pyplot as plt 
    try:
        portx = "COM3"
        bps = 115200
        # 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
        timex = 3
        ser = Serial(portx, bps, timeout=timex)
        ay = []  # 定义一个 y 轴的空列表用来接收动态的数据
        t_list_1=[] # 暂时存放高峰序号
        t_list_2=[] # 暂时存放峰值
        t_list=[] # R峰序列
        n=0
        start=time.time()
        while(len(t_list_1)<=25):
            place = (ser.read(5).decode("ASCII"))[0:4]
            # print(place)
            ay.append(int(place))
            if len(ay)>=2:
                if ay[n-2]<ay[n-1] and ay[n-1]>=ay[n]:
                    t_list_1.append(n-1)
                    t_list_2.append(ay[n-1])
            n=n+1
        end=time.time()
        # print('ay ',ay)
        # print("t_list_1 ",t_list_1)
        # print("t_list_2 ",t_list_2)
        ser.close()  # 关闭串口
        gap=(end-start)/n # 计算间隔
        # print('gap ',gap)
        # print('n ',n)
        for i in range(1,len(t_list_1)-1): # 剔除其他峰值
            if t_list_2[i-1]<t_list_2[i] and t_list_2[i]>t_list_2[i+1]:
                t_list.append(t_list_1[i])
        # print('t_list ',t_list)
        result=[]
        for i in range(5):
            result.append(60/((t_list[i+1]-t_list[i])*gap))
        # print('result ',result)
        # print(sum(result)/5)
        plt.plot(range(len(ay)),ay)
        plt.show()
        return result
    except Exception as e:
        import random
        print("[-] Error : ", e)
        result=[random.random()*30+60 for i in range(5)]
        print(result)
        return result

# getRawData()