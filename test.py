import database
import pygrib 
import numpy


gfs = database.GFS()
#dat.download_latest()
gfs.load('latest.grb2')
max_temperatures = gfs.file.select(name='Maximum temperature')[0]
deneme = gfs.file[3]
gfs.init_wind_data()
print(gfs.wind_data)
#for e in gfs.file:
#    print(e)
max_temperatures_2d_array = (max_temperatures.values)
print(max_temperatures_2d_array.shape)
#numpy.savetxt("max_temperatures_2d_array.csv", max_temperatures_2d_array, delimiter=",")
#print(gfs.file)
print(gfs.get_date())
#gfs.init_wind_data()
