from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import threading
import os
import shutil
import zipfile
import socket







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
archivo1 = os.path.join(lugar_del_archivo, "world.zip")
archivo2 = os.path.join(lugar_del_archivo, "world_nether.zip")
archivo3 = os.path.join(lugar_del_archivo, "world_the_end.zip")

def overworld():
    global drive
    lugar_del_archivo = os.path.dirname(os.path.abspath(__file__))
    archivo1 = os.path.join(lugar_del_archivo, "world1.zip")
    archivo2 = os.path.join(lugar_del_archivo, "world2.zip")
    archivo3 = os.path.join(lugar_del_archivo, "world.zip")
    try:
        os.remove(archivo1)
    except IOError:
        pass
    print("Descargando el overworld")
    with open("world_id.txt", "r") as w:
        id1 = w.read()
    overworld1 = drive.CreateFile({'id': id1})
    overworld1.GetContentFile(archivo1)



    print("overworld descargado")

    def extraer():
        global lugar_del_archivo
        global archivo3
        global archivo1
        global archivo2
        print("extrayendo el overworld")
        archivo4 = os.path.join(lugar_del_archivo, "world")
        with zipfile.ZipFile("world.zip", 'r') as zip_ref:
            zip_ref.extractall(archivo4)
        try:
            os.remove(archivo1)
            os.remove(archivo2)
            os.remove(archivo3)
        except IOError:
            pass
        print("overworld extraido, se ha acabado el proceso del overworld")
    extraer()

    
    
def nether():
    global drive
    lugar_del_archivo = os.path.dirname(os.path.abspath(__file__))
    archivo2 = os.path.join(lugar_del_archivo, "world_nether.zip")
    try:
        os.remove(archivo2)
    except IOError:
        pass
    print("descargando el nether")
    with open("world_nether_id.txt", "r") as w:
        id2 = w.read()
    nether = drive.CreateFile({'id': id2})
    nether.GetContentFile(archivo2)
    print("nether descargado")
    def extraer():
        global lugar_del_archivo
        global archivo2
        print("extrayendo el nether")
        archivo5 = os.path.join(lugar_del_archivo, "world_nether")
        with zipfile.ZipFile("world_nether.zip", 'r') as zip_ref:
            zip_ref.extractall(archivo5)
        try:
            os.remove(archivo2)
        except IOError:
            pass
        print("nether extraido, se ha acabado el proceso del nether")
    extraer()


def the_end():
    global drive
    lugar_del_archivo = os.path.dirname(os.path.abspath(__file__))
    archivo3 = os.path.join(lugar_del_archivo, "world_the_end.zip")
    try:
        os.remove(archivo3)
    except IOError:
        pass
    print("descargando el end")
    with open("world_the_end_id.txt", "r") as w:
        id3 = w.read()
    end = drive.CreateFile({'id': id3})
    end.GetContentFile(archivo3)
    print("end descargado")
    
    def extraer():
        global lugar_del_archivo
        global archivo3
        print("extrayendo el end")
        archivo6 = os.path.join(lugar_del_archivo, "world_the_end")
        with zipfile.ZipFile("world_the_end.zip", 'r') as zip_ref:
            zip_ref.extractall(archivo6)
        try:
            os.remove(archivo3)
        except IOError:
            pass
        print("end extraido, acabado el proceso del end")
    extraer()


    
    
t_overworld = threading.Thread(target=overworld)
t_overworld.start()
t_nether = threading.Thread(target=nether)
t_nether.start()
t_the_end = threading.Thread(target=the_end)
t_the_end.start()



