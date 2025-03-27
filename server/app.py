import tornado.httpserver
import tornado.web
import tornado.ioloop
import hashlib
import pymysql
import os,shutil,time,sys
import SEAL_service as seal
#from mysql import connector

mysql_settings = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "H235*+aasdc.t$",
    "db": "webproject",
    "charset": "utf8"
}
def checkid_number(id_number):
    for i in id_number:
        if i not in '0123456789X':
            print('身份证出错：',i)
            return False
    return True
def checkpassword(password):
    if len(password)!=64:
        return False
    else:
        for i in password:
            if i not in 'abcdef0123456789':
                return False
    return True
def checkmsg(name,age,gender,rate,id_number):
    strangestr='-+*/.,;\'"[]\\=-()&*%^#$!@~`<>?:\{\}，。、？；’：“”【】《》|——……￥·！'
    #检查姓名信息
    if name== '' or age == '' or gender == '' or rate == '' or id_number == '':
        return False
    for i in name:
        if i in strangestr:
            print('姓名出错：',i)
            return False
    #检查年龄信息
    for i in age:
        if i not in '0123456789':
            print('年龄出错：',i)
            return False
    #检查性别信息
    for i in gender:
        if i in strangestr:
            print('性别出错：',i)
            return False
    #检查心率状况信息
    for i in rate:
        if i in strangestr:
            print('心率状况出错：',i)
            return False
    #检查身份证信息
    for i in id_number:
        if i not in '0123456789X':
            print('身份证出错：',i)
            return False
    return True
class Login(tornado.web.RequestHandler):
    def post(self):
        password = self.get_argument('password')
        db_connect = pymysql.connect(**mysql_settings)
        cursor = db_connect.cursor()
        select_sql = 'select * from doctor where key_hash=%s'
        cursor.execute(select_sql,password)
        db_connect.commit()
        db_connect.close()
        result = cursor.fetchall()

        if result == ():
            cursor.close()
            self.write('用户不存在')
        else:
            user_info = result[0]
            if password == user_info[0]:
                cursor.close()
                self.write('登陆成功')
            else:
                self.write('用户名或密码错误')


class Register(tornado.web.RequestHandler):
    def post(self):
        password = self.get_argument('password')
        if checkpassword(password):
            db_connect = pymysql.connect(**mysql_settings)
            cursor = db_connect.cursor()
            select_sql = 'select key_hash from doctor where key_hash=%s'
            cursor.execute(select_sql,password)
            db_connect.commit()
            if len(cursor.fetchall())!=0:
                cursor.close()
                db_connect.close()
                self.write('用户已存在，请重新输入')
            else:
                insert_sql = 'insert into doctor(key_hash) values(%s)'
                cursor.execute(insert_sql,password)
                #create_sql = 'create table {}(result_path varchar(500),AES_path varchar(500))'.format(password)
                create_sql = 'create table {}(name varchar(50),age varchar(10),gender varchar(10),rate varchar(50),id_number varchar(100),add_time varchar(100))'.format(password)
                cursor.execute(create_sql)
                cursor.close()
                db_connect.commit()
                db_connect.close()
                upload_path=os.path.join(os.path.dirname(__file__),'user_key')  
                #提取表单中‘name’为‘file’的文件元数据
                file_metas=self.request.files['user_key']    
                for meta in file_metas:
                    filename=meta['filename']
                    filepath=os.path.join(upload_path,filename)
                    #有些文件需要已二进制的形式存储，实际中可以更改
                    with open(filepath,'wb') as up:      
                        up.write(meta['body'])
                self.write('注册成功')
        else:
            self.write('非法输入！')
class UploadFileHandler(tornado.web.RequestHandler):
    def post(self):
        t=time.strftime("%Y%m%d-%H.%M", time.localtime())
        password = self.get_argument('password')
        id_number = self.get_argument('id_number')
        if checkpassword(password) and checkid_number(id_number):
            db_connect = pymysql.connect(**mysql_settings)
            cursor = db_connect.cursor()
            select_sql = 'select id_number from {} where id_number="{}"'.format(password,id_number)
            cursor.execute(select_sql)
            db_connect.commit()
            if len(cursor.fetchall())!=0:
                #文件的暂存路径
                upload_path=os.path.join(os.path.dirname(__file__),'packet_save')  
                #提取表单中‘name’为‘file’的文件元数据
                file_metas=self.request.files['enc_file']    
                for meta in file_metas:
                    filename=meta['filename']
                    enc_path=os.path.join(upload_path,filename)
                    #有些文件需要已二进制的形式存储，实际中可以更改
                    with open(enc_path,'wb') as up:      
                        up.write(meta['body'])
                filepath=os.path.join(upload_path,t)
                temp=os.path.join(os.path.dirname(__file__),'user_key',password)
                f1=open(temp,'rb')
                parms_Rel=f1.read()
                f2=open(enc_path,'rb')
                data=f2.read()
                f3=open(filepath,'wb')
                f3.write(parms_Rel+data)
                f1.close()
                f2.close()
                f3.close()
                os.remove(enc_path)
                result_temp_path=seal.calculate(3,filepath)
                result_path=os.path.join(os.path.dirname(__file__),'result',password,genearteMD5(id_number))
                folder = os.path.exists(result_path) 
                if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
                    os.makedirs(result_path)
                shutil.move(result_temp_path,result_path)
                os.rename(os.path.join(result_path,os.path.basename(result_temp_path)),os.path.join(result_path,t))

                #文件的暂存路径
                upload_path1=os.path.join(os.path.dirname(__file__),'AES_save')  
                AES_save_path=os.path.join(os.path.dirname(__file__),'AES_save',password,genearteMD5(id_number))
                folder = os.path.exists(AES_save_path) 
                if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
                    os.makedirs(AES_save_path)
                
                #提取表单中‘name’为‘file’的文件元数据
                file_metas1=self.request.files['AES_file']    
                for meta in file_metas1:
                    AES_path=os.path.join(AES_save_path,t)
                    #有些文件需要已二进制的形式存储，实际中可以更改
                    with open(AES_path,'wb') as up1:      
                        up1.write(meta['body'])
                insert_sql = 'insert into {}(result_path,AES_path) values("{}","{}")'.format(genearteMD5(id_number),os.path.join(result_path,t),AES_path)
                cursor.execute(insert_sql)
                cursor.close()
                db_connect.commit()
                db_connect.close()
            else:
                cursor.close()
                db_connect.commit()
                db_connect.close()
                self.write('用户不存在')
        else:
            self.write('数据不合法！')
class DblistHandler(tornado.web.RequestHandler):
    def get(self):
        password=self.get_argument('password')
        id_number=self.get_argument('id_number')
        str=''

        if checkpassword(password) and checkid_number(id_number):
            db_connect = pymysql.connect(**mysql_settings)
            cursor = db_connect.cursor()
            # 查找用户是否存在
            select_sql = 'select key_hash from doctor where key_hash="{}"'.format(password)
            cursor.execute(select_sql)
            db_connect.commit()
            result=cursor.fetchall()
            if len(result)!=0:
                #查找结果密文列表
                select_sql = 'select result_path from {}'.format(genearteMD5(id_number))
                cursor.execute(select_sql)
                db_connect.commit()
                result=cursor.fetchall()
                
                for i in range(len(result)):
                    if(i==len(result)-1):
                        str+=''.join(result[i])
                    else:
                        str+=''.join(result[i])+','
                cursor.close()
                db_connect.close()
        self.write(str)
class DownloadHandler(tornado.web.RequestHandler):
     # 设置允许跨域
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
        self.set_header("Access-Control-Allow-Methods", "POST,GET,OPTIONS")

    def get(self):
        # 获取参数
        # 读取的内存大小，一般会在保存文件的时候记录下来，最好比源文件大
        password=self.get_argument('password', None)
        id_number=self.get_argument('id_number', None)
        if checkpassword(password) and checkid_number(id_number):
            db_connect = pymysql.connect(**mysql_settings)
            cursor = db_connect.cursor()
            select_sql = 'select id_number from {} where id_number="{}"'.format(password,id_number)
            cursor.execute(select_sql)
            db_connect.commit()
            result=cursor.fetchall()
            if len(result)!=0:
                buf_size = 4096
                filename=self.get_argument('filename', None)
                filename=filename.replace("..","")
                if filename[:7]!='result/':
                    filename='result/'+filename
                if not filename:
                    self.write({"error":"文件名称为空"})
                    return
                # 设置传输的文件类型，有很多例如png/pdf等等 取决于不同情形，这边我用octet-stream
                self.set_header ('Content-Type', 'application/octet-stream')
                # 设置文件保存名，也就是你下载完成显示的名称
                self.set_header ('Content-Disposition', 'attachment; filename='+filename)
                path='./'+filename
                with open( path, 'rb') as f:
                    while True:
                        data = f.read(buf_size)
                        if not data:
                            break
                        self.write(data)
        self.finish()
class Add_PatientHandler(tornado.web.RequestHandler):
    def post(self):
        password=self.get_argument('password')
        name=self.get_argument('name')
        age=self.get_argument('age')
        gender=self.get_argument('gender')
        rate=self.get_argument('rate')
        id_number=self.get_argument('id_number')
        add_time=self.get_argument('add_time')
        #check
        if checkpassword(password) and checkmsg(name,age,gender,rate,id_number):
            db_connect = pymysql.connect(**mysql_settings)
            cursor = db_connect.cursor()
            select_sql = 'select id_number from {} where id_number="{}"'.format(password,id_number)
            cursor.execute(select_sql)
            db_connect.commit()
            if len(cursor.fetchall())!=0:
                cursor.close()
                db_connect.close()
                self.write('身份证号已存在，请重新输入')
            else:
                # select_sql = 'select result_path from {}'.format(password)
                insert_sql = 'insert into {}(name,age,gender,rate,id_number,add_time) values("{}","{}","{}","{}","{}","{}")'.format(password,name,age,gender,rate,id_number,add_time)
                cursor.execute(insert_sql)
                create_sql = 'create table {}(result_path varchar(500), AES_path varchar(500))'.format(genearteMD5(id_number))
                cursor.execute(create_sql)
                db_connect.commit()
                cursor.close()
                db_connect.close()
                self.write('添加成功')
        self.finish()
        
class Change_PatientHandler(tornado.web.RequestHandler):
    def post(self):
        password=self.get_argument('password')
        name=self.get_argument('name')
        age=self.get_argument('age')
        gender=self.get_argument('gender')
        rate=self.get_argument('rate')
        id_number=self.get_argument('id_number')
        if checkpassword(password) and checkmsg(name,age,gender,rate,id_number):
            db_connect = pymysql.connect(**mysql_settings)
            cursor = db_connect.cursor()
            change_sql = 'update {} set name="{}",age="{}",gender="{}",rate="{}" where id_number="{}"'.format(password,name,age,gender,rate,id_number)
            cursor.execute(change_sql)
            db_connect.commit()
            cursor.close()
            db_connect.close()
        self.finish()



class Delete_PatientHandler(tornado.web.RequestHandler):
    def post(self):
        password=self.get_argument('password')
        id_number=self.get_argument('id_number')
        if checkpassword(password) and checkid_number(id_number):
            db_connect = pymysql.connect(**mysql_settings)
            cursor = db_connect.cursor()
            delete_sql1 = 'delete from {} where id_number="{}"'.format(password,id_number)
            cursor.execute(delete_sql1)
            delete_sql2 = 'drop table {}'.format(genearteMD5(id_number))
            cursor.execute(delete_sql2)
            db_connect.commit()
            cursor.close()
            db_connect.close()
        self.finish()
class PatientlistHandler(tornado.web.RequestHandler):
    def get(self):
        password=self.get_argument('password')
        str=''
        if checkpassword(password):
            db_connect = pymysql.connect(**mysql_settings)
            cursor = db_connect.cursor()
            select_sql = 'select * from {}'.format(password)
            cursor.execute(select_sql)
            db_connect.commit()
            result=cursor.fetchall()
            if(len(result)!=0):
                for i in range(len(result)):
                    for j in range(len(result[i])):
                        if(j==len(result[i])-1):
                            if(i==len(result)-1):
                                str+=''.join(result[i][j])
                            else:
                                str+=''.join(result[i][j])+','
                        else:
                            str+=''.join(result[i][j])+'|'
            cursor.close()
            db_connect.close()
        self.write(str)
def genearteMD5(str):
    # 创建md5对象
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()
app = tornado.web.Application([
    ('/login', Login),
    ('/register', Register),
    ('/file',UploadFileHandler),
    ('/add_patient',Add_PatientHandler),
    ('/change_patient',Change_PatientHandler),
    ('/delete_patient',Delete_PatientHandler),
    ('/patient_list',PatientlistHandler),
    ('/dblist',DblistHandler),
    ('/download',DownloadHandler)
])

if __name__ == '__main__':
    server = tornado.httpserver.HTTPServer(app, max_buffer_size=1536000000)
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
