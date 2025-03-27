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

