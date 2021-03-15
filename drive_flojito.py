from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import threading
import os
import shutil
import time




gauth = GoogleAuth()
gauth.LoadCredentialsFile("DBCRD.txt")
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile("DBCRD.txt")
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



def overworld2():
    global archivo_overworld
    print("subiendo el overworld")
    with open("world_id.txt", "r") as w:
        id1 = w.read()
    folder1 = drive.CreateFile({'id': id1})
    folder1.SetContentFile(archivo_overworld)
    folder1.Upload()
    print("El segundo trozo del overworld se ha subido")
t_overworld2 = threading.Thread(target=overworld2)
t_overworld2.start()


def nether():
    global archivo_nether
    print("subiendo el nether")
    with open("world_nether_id.txt", "r") as w:
        id2 = w.read()
    folder2 = drive.CreateFile({'id': id2})
    folder2.SetContentFile(archivo_nether)
    folder2.Upload()
    print("nether subido")
t_nether = threading.Thread(target=nether)
t_nether.start()


def end():
    global archivo_end
    print("subiendo el end")
    with open("world_the_end_id.txt", "r") as w:
        id3 = w.read()
    folder3 = drive.CreateFile({'id': id3})
    folder3.SetContentFile(archivo_end)
    folder3.Upload()
    print("end subido")
t_end = threading.Thread(target=end)
t_end.start()




