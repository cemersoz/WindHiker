import pygrib
import os
import time

class Database(object):
    def __init__(self):
        self.files = []
        pass

    def download(url,file_name):
        os.system("curl %s -o %s" % (url,file_name))

    def load(self,file_name):
        self.files.append(pygrib.open(file_name))
        return self.files[-1]

    def get_date(self):
        #year,month,day
        date = time.gmtime()
        return (date[0],date[1],date[2])

class GFS(Database):
    def __init__(self):
        Database.__init__(self)

    def download_latest(self,name="latest.grb2"):
        #random url
        Database.download("https://nomads.ncdc.noaa.gov/data/gfsanl/201711/20171104/gfsanl_4_20171104_0000_006.grb2",name)
