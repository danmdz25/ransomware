import os
import pyaes
#  abrir arquivos criptografado

file_name = 'course.txt.ransomwaretroll'
file = open(file_name,'rb')
file_data= file.read()
file.close()

# Chave de decrypt
key = b'testeransomwares'
aes=pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

#  remover o arquivo criptografado

os.remove(file_name)


#criar um novo arquivo descriptografado

new_file ='course.txt'
new_file=open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close