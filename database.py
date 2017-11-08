import pygrib
import os
import time

class Database(object):
    def __init__(self):
        self.file = None
        pass

    def download(url,file_name):
        os.system("curl %s -o %s" % (url,file_name))

    def load(self,file_name):
        self.file = pygrib.open(file_name)
        return self.file

    def get_date(self):
        #year,month,day
        date = time.gmtime()
        return (date[0],date[1],date[2])

class GFS(Database):
    def __init__(self):
        Database.__init__(self)
        #wind_data(hPa) returns the indeces of the corresponding
        #u and v components of the wind from the file as a tuple
        #ex: wind_data(1000)= (39,40)
        #after finding the index you can query the according data
        #with file[i].values (returns 2d array of value, indexed
        #by lat. and long.)
        self.wind_data = {}
        #su lanet seyi loopla lutfen
       
        

    def download_latest(self,name="latest.grb2"):
        #random url
        Database.download("https://nomads.ncdc.noaa.gov/data/gfsanl/201711/20171104/gfsanl_4_20171104_0000_006.grb2",name)

    def init_wind_data(self):
        for line in self.file:
            line = str(line)
            if "U component of wind:" in line:
                if " Pa" in line and "levels" not in line:
                    Pa = line.find(' Pa')
                    level = line.find('level')
                    colon = line.find(':')
                    index = int(line[:colon])
                    self.wind_data[line[level+6:Pa]] = (index,index+1)
                    print(line[level+6:Pa])





