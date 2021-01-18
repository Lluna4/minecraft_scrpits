from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import threading
import os
import shutil
import time




gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile("mycreds.txt")
drive = GoogleDrive(gauth)

lugar_del_archivo = os.path.dirname(os.path.abspath(__file__))
archivo = os.path.join(lugar_del_archivo, "world.zip")
archivo2 = os.path.join(lugar_del_archivo, "world_nether.zip")
archivo3 = os.path.join(lugar_del_archivo, "world_the_end.zip")

try:
    os.remove(archivo)
    os.remove(archivo2)
    os.remove(archivo3)
except IOError:
    pass

archivo4 = os.path.join(lugar_del_archivo, "world")
archivo5 = os.path.join(lugar_del_archivo, "world_nether")
archivo6 = os.path.join(lugar_del_archivo, "world_the_end")

shutil.make_archive(archivo4, 'zip', archivo4)
print("empaquetando el overworld")
shutil.make_archive(archivo5, 'zip', archivo5)
print("empaquetando el nether, el overworld ya esta empaquetado")
shutil.make_archive(archivo6, 'zip', archivo6)
print("empaquetando el end, el nether ya esta empaquetado")

lugar_del_archivo = os.path.dirname(os.path.abspath(__file__))
archivo_overworld = os.path.join(lugar_del_archivo, "world.zip")
archivo_nether = os.path.join(lugar_del_archivo, "world_nether.zip")
archivo_end = os.path.join(lugar_del_archivo, "world_the_end.zip")

archivo_overworld1 = os.path.join(lugar_del_archivo, "world1.zip")
archivo_overworld2 = os.path.join(lugar_del_archivo, "world2.zip")
peso_overworld = os.path.getsize(archivo_overworld)
chunk_peso = peso_overworld / 2
chunk_peso_int = int(chunk_peso)
with open(archivo_overworld, "rb") as f1_r:
    chunk = f1_r.read(chunk_peso_int)
    with open(archivo_overworld1, "wb") as f2_w:
        f2_w.write(chunk)
    chunk2 = f1_r.read(chunk_peso_int)
    with open(archivo_overworld2, "wb") as f3_w:
        f3_w.write(chunk2)

def overworld1():
    global archivo_overworld1
    print("subiendo el primer trozo del overworld")
    folder0 = drive.CreateFile({'id': "1RJLIXvN8rPBE5qzC77WNHzRv89vvEr-6"})
    folder0.SetContentFile(archivo_overworld1)
    folder0.Upload()
    print("el primer trozo del overworld se ha subido")
    
t_overworld1 = threading.Thread(target=overworld1)
t_overworld1.start()

def overworld2():
    global archivo_overworld2
    print("subiendo el segundo trozo del overworld")
    folder1 = drive.CreateFile({'id': "101mrvpCYNvTxHQjKry90-WnwFYnAJZbv"})
    folder1.SetContentFile(archivo_overworld2)
    folder1.Upload()
    print("El segundo trozo del overworld se ha subido")
t_overworld2 = threading.Thread(target=overworld2)
t_overworld2.start()


def nether():
    global archivo_nether
    print("subiendo el nether")
    folder2 = drive.CreateFile({'id': "1SxEsnVlStflTSPRUnQryBfqQAZHK_LSq"})
    folder2.SetContentFile(archivo_nether)
    folder2.Upload()
    print("nether subido")
t_nether = threading.Thread(target=nether)
t_nether.start()


def end():
    global archivo_end
    print("subiendo el end")
    folder3 = drive.CreateFile({'id': "1H5fSzKSYNf41lQiePPil3SduHOse-2V_"})
    folder3.SetContentFile(archivo_end)
    folder3.Upload()
    print("end subido")
t_end = threading.Thread(target=end)
t_end.start()




