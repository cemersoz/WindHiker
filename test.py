import database
import pygrib 
gfs = database.GFS()
#dat.download_latest()
gfs.load('latest.grb2')
grb = gfs.files[-1].select(name='Maximum temperature')[0]
nebu = (grb.data()[1][360][719])
print(nebu)
print(gfs.get_date())
