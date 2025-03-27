from operator import ge
import os
from Crypto.Cipher import AES
import hashlib
import io
import requests
# url='http://192.168.92.132:8888'
import configparser
config = configparser.ConfigParser()
config.read('./config.ini')
url=config['DEFAULT']['url']
class AESUtil:
    def __pad(self, text):
        """填充方式，加密内容必须为16字节的倍数，若不足则使用self.iv进行填充"""
        text_length = len(text)
        amount_to_pad = AES.block_size - (text_length % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        pad = chr(amount_to_pad)
        pad=bytes(pad,encoding="ascii")
        return text + pad * amount_to_pad

    def __unpad(self, text):
        #  ASCII 数值
        pad=ord(text[-1:])
        return text[:-pad]

    def aes_encrypt(self, plain_data, key, iv):
        """
        AES CBC 128
        CBC加密需要一个十六位的key(密钥)和一个十六位iv(偏移量)
        加密函数，如果data不是16的倍数【加密文本data必须为16的倍数！】，那就补足为16的倍数
        :param plain_data:明文数据 16位
        :param key:  16位
        :param iv:16位
        """
        cipher = AES.new(key, AES.MODE_CBC, iv)  # 设置AES加密模式 此处设置为CBC模式

        # 填充数据
        pad_data = self.__pad(text=plain_data)

        encrypted_data = cipher.encrypt(pad_data)  # aes加密
        # b2a_hex encode  将二进制转换成16进制,返回的二进制数据的十六进制表示。每一个字节的数据转换成相应的2位十六进制表示。
        # result = binascii.b2a_hex(encrypted_data)
        return encrypted_data

    def aes_decryppt(self, enc_data, key, iv):
        """
        AES 解密
        :param key:
        :param data:
        """
        cipher = AES.new(key, AES.MODE_CBC, iv)
        dec_data = cipher.decrypt(enc_data)

        unpad_data = self.__unpad(dec_data)
        # 字符串转16进制
        # result = binascii.hexlify(unpad_data)
        return unpad_data

    def enc_file(self, plain_file_path, enc_file_path, key):
        try:
            # 加密向量
            if len(key)<16:
                key=key+'0'*(16-len(key))
            elif len(key)>16:
                key=key[:16]
            key=str.encode(key)
            iv = key

            with open(plain_file_path, 'rb') as fileobj:
                content = fileobj.read()
                # 加密文件
                enc_content = self.aes_encrypt(plain_data=content, key=key, iv=iv)
            fileobj.close()

            #获取key文件的sha256值
            m = hashlib.sha256()
            file = io.FileIO(plain_file_path,'r')
            bytes = file.read(1024)
            while(bytes != b''):
                m.update(bytes)
                bytes = file.read(1024)
                md5value = m.hexdigest()
                md5value1=str.encode(md5value)
            file.close()

            with open(enc_file_path, 'wb') as f:  # 以二进制写类型打开
                f.write(md5value1)
                f.write(enc_content)  # 写入文件
            f.close()
            os.remove(plain_file_path)
            return True,md5value1
        except:
            return False,''

    def dec_file(self, enc_file_path, dec_file_path, key):
        # 向量
        if len(key)<16:
            key=key+'0'*(16-len(key))
        elif len(key)>16:
            key=key[:16]
        # 向量
        key=str.encode(key)
        iv = key
        with open(enc_file_path, 'rb') as fileobj:
            content = fileobj.read()
            sha256_1=content[:64]
            content1=content[64:]
            # 解密文件
            dec_content = self.aes_decryppt(enc_data=content1, key=key, iv=iv)
        fileobj.close()

        with open(dec_file_path, 'wb') as f:  # 以二进制写类型打开
            f.write(dec_content)  # 写入文件
        f.close()
        sha256_2=sha256_1.decode('ascii')

        #获取解密出来文件的sha256值
        m = hashlib.sha256()
        file = io.FileIO(dec_file_path,'r')
        bytes = file.read(1024)
        while(bytes != b''):
          m.update(bytes)
          bytes = file.read(1024)
        file.close()
        sha256value = m.hexdigest()

        if(sha256value==sha256_2):
            return True,sha256_2
        else:
            return False,sha256value
    
    def enc_AES(self, plain_file_path, enc_file_path, key):
        try:
            # 加密向量
            if len(key)<16:
                key=key+'0'*(16-len(key))
            elif len(key)>16:
                key=key[:16]
            key=str.encode(key)
            iv = key

            with open(plain_file_path, 'rb') as fileobj:
                content = fileobj.read()
                # 加密文件
                enc_content = self.aes_encrypt(plain_data=content, key=key, iv=iv)
            fileobj.close()

            with open(enc_file_path, 'wb') as f:  # 以二进制写类型打开
                f.write(enc_content)  # 写入文件
            f.close()
            os.remove(plain_file_path)
            return True
        except:
            return False





def dec_file(enc_file_path, dec_file_path, key):
    aes_util=AESUtil()
    [flag,sha256]=aes_util.dec_file(enc_file_path=enc_file_path, dec_file_path=dec_file_path, key=key)
    os.remove(dec_file_path)
    if flag:
        return True,sha256
    else:
        return False,''

def enc_file(plain_file_path, enc_file_path, key):
    aes_util=AESUtil()
    [flag,key_hash]=aes_util.enc_file(plain_file_path=plain_file_path, enc_file_path=enc_file_path, key=key)
    if(flag):
        return True,key_hash
    else:
        return False,key_hash

def dec_key(enc_file_path, dec_file_path, key):
    aes_util=AESUtil()
    aes_util.dec_file(enc_file_path=enc_file_path, dec_file_path=dec_file_path, key=key)

def enc_AES(plain_file_path, enc_file_path, key):
     aes_util=AESUtil()
     aes_util.enc_file(plain_file_path=plain_file_path, enc_file_path=enc_file_path, key=key)
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

#登录
def login(path,hash):
    try:
        post_data = {'password': hash}
        response=requests.post(url=url+path,data=post_data)
        if response.text =='登陆成功':
            return True
        else:
            return False
    except:
        return False
#注册
def register(path,hash,file):
    try:
        post_data = {'password': hash}
        files={
            'user_key':(hash,open(file,'rb').read())
        }
        response=requests.post(url=url+path,data=post_data,files=files)
        if response.text=='注册成功':
            return True
        else:
            return False
    except:
        return False

#上传密文
def file_post(hash,id_number,file1,file2):
    try:
        post_data={'password': hash,'id_number':id_number}
        # print(post_data)
        # print(file1,file2)
        files={
            'enc_file':(file1,open(file1,'rb').read()),
            'AES_file':('temp_AES',open(file2,'rb').read())
        }
        response=requests.post(url=url+'/file',data=post_data,files=files)
        return True
    except:
        return False

#增加病人
def add_patient(hash,name,age,gender,rate,id_number,t):
    try:
        post_data={
            'password':hash,
            'name':name,
            'age':age,
            'gender':gender,
            'rate':rate,
            'id_number':id_number,
            'add_time':t
        }
        if not checkmsg(name,age,gender,rate,id_number):
            return False,''
        response=requests.post(url=url+'/add_patient',data=post_data)
        if(response.status_code==200):
            return True,response.text
        else:
            return False,''
    except:
        return False,''

#删除病人
def delete_patient(hash,id_number):
    try:
        post_data={
            'password':hash,
            'id_number':id_number
        }
        response=requests.post(url=url+'/delete_patient',data=post_data)
        if(response.status_code==200):
            return True
        else:
            return False
    except:
        return False
#修改病人信息
def change_patient(hash,name,age,gender,rate,id_number):
    try:
        post_data={
            'password':hash,
            'name':name,
            'age':age,
            'gender':gender,
            'rate':rate,
            'id_number':id_number,
        }
        if not checkmsg(name,age,gender,rate,id_number):
            return False
        response=requests.post(url=url+'/change_patient',data=post_data)
        if(response.status_code==200):
            return True
        else:
            return False
    except:
        return False

#获取病人列表
def patient_list(hash):
    response=requests.get(url=url+'/patient_list?password='+hash)
    if(response.status_code==200):
        return response
    else:
        return False

#获取列表
def dblist(password,hash):
    response=requests.get(url=url+'/dblist?password='+password+'&id_number='+hash)
    if(response.status_code==200):
        return True, response
    else:
        return False,''

#下载密文
def download(path):
    response=requests.get(url=url+'/download?filename='+path)
    return response

