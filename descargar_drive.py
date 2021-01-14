from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import threading
import os
import shutil
import zipfile

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
    overworld1 = drive.CreateFile({'id': "1RJLIXvN8rPBE5qzC77WNHzRv89vvEr-6"})
    overworld1.GetContentFile(archivo1)
    overworld2 = drive.CreateFile({'id': "101mrvpCYNvTxHQjKry90-WnwFYnAJZbv"})
    overworld2.GetContentFile(archivo2)

    with open(archivo1, "rb") as f1_r:
        mitad1 = f1_r.read()
        with open(archivo3, "wb") as f2_w:
            f2_w.write(mitad1)
    
    with open(archivo2, "rb") as f3_r:
        mitad2 = f3_r.read()
        with open(archivo3, "ab") as f4_w:
            f4_w.write(mitad2)

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
    nether = drive.CreateFile({'id': "1SxEsnVlStflTSPRUnQryBfqQAZHK_LSq"})
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
    end = drive.CreateFile({'id': "1H5fSzKSYNf41lQiePPil3SduHOse-2V_"})
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



