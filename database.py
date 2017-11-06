import pygrib
import os
import time

class Database(object):
    def __init__(self):
        pass

    def download(url,file_name):
        os.system("curl %s -o %s" % (url,file_name))

    def open_grib(file_name):
        return pygrib.open(file_name)

    def get_date(self):
        #year,month,day
        date = time.gmtime()
        return (date[0],date[1],date[2])

class GFS(Database):
    def __init__(self):
        Database.__init__(self)

    def download_latest(self):
        #random url
        Database.download("https://nomads.ncdc.noaa.gov/data/gfsanl/201711/20171104/gfsanl_4_20171104_0000_006.grb2","test.grb2")