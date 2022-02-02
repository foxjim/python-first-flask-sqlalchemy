from Cryptodome.Cipher import AES
import base64
from binascii import b2a_hex, a2b_hex


class AESUtils():
    key = "liuguixiu@202112"
    model = AES.MODE_ECB  # 定义模式
    aes = None

    def __init__(self):
        self.aes = AES.new(self.key.encode(), self.model)

    def addToLength16(self,par):
        par = par.encode();
        while len(par) % 16 != 0:  # 对字节型数据进行长度判断
            par += b'\x00'  # 如果字节型数据长度不是16倍整数就进行 补充
        return par

    def encrypt(self,content):
        content = self.addToLength16(content)
        cipher_text = self.aes.encrypt(content);
        return b2a_hex(cipher_text)

    def decode(self,content):
        content = self.aes.decrypt(content)
        return content

if __name__ == '__main__':
    str = '0000000000123455522678'

    aes = AESUtils()

    pwd = aes.encrypt(str)
    print(pwd)
    print(a2b_hex(aes.decode(pwd)))