from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import threading
import os
import shutil


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
shutil.make_archive(archivo5, 'zip', archivo5)
shutil.make_archive(archivo6, 'zip', archivo6)

lugar_del_archivo = os.path.dirname(os.path.abspath(__file__))
archivo_overworld = os.path.join(lugar_del_archivo, "world.zip")
archivo_nether = os.path.join(lugar_del_archivo, "world_nether.zip")
archivo_end = os.path.join(lugar_del_archivo, "world_the_end.zip")

folder = drive.CreateFile({'id': "1RJLIXvN8rPBE5qzC77WNHzRv89vvEr-6"})
folder.SetContentFile(archivo_overworld)
folder.Upload()

folder = drive.CreateFile({'id': "1SxEsnVlStflTSPRUnQryBfqQAZHK_LSq"})
folder.SetContentFile(archivo_nether)
folder.Upload()

folder = drive.CreateFile({'id': "1H5fSzKSYNf41lQiePPil3SduHOse-2V_"})
folder.SetContentFile(archivo_end)
folder.Upload()


