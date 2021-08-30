# Gets inputs: LatLong, time, pressure, temp, 
# and optionally:
# Azimuth of panel surface, Degrees tilt from horizontal of panel, 
# Solar constant (W/m2), Shadow-band width (cm), Shadow-band radius (cm), 
# Shadow-band sky factor, Interval of a measurement period (sec)
def ghisolpos( latitude, longitude, dt, pressure, temperature, panelazimuth = '180', paneltilt = '0', solarconstant = '1367', shadowbandwidth = '7.6', shadowbandradius = '31.7', shadowbandfactor = '0.04'):      
   from datetime import datetime
   from pandas import read_csv
   import pandas as pd
   d = datetime.strptime(dt, '%d/%m/%Y %H:%M:%S')
   year = d.year
   month = d.month
   day = d.day
   hour = d.hour
   minute = d.minute
   url = 'https://www.nrel.gov/midc/apps/solpos.pl?syear={year}&smonth={month}&sday={day}&eyear={year}&emonth={month}&eday={day}&step=1&stepunit=1&latitude={latitude}&longitude={longitude}&timezone=5.5&press={pressure}&temp={temperature}&aspect={panelazimuth}&tilt={paneltilt}&solcon={solarconstant}&sbwid={shadowbandwidth}&sbrad={shadowbandradius}&sbsky={shadowbandfactor}&interval=0&field=14&zip=0'.format(year = year, month = month, day = day, latitude = latitude, longitude = longitude, temperature = temperature, pressure = pressure, panelazimuth = panelazimuth, paneltilt = paneltilt, solarconstant = solarconstant, shadowbandwidth = shadowbandwidth, shadowbandradius = shadowbandradius, shadowbandfactor = shadowbandfactor) 

# Calls the Solpos with those inputs and returns a single GHI value for that time. 
   a = read_csv(url)
   a['datetime'] = a['Date'] + " " + a['Time']
   a['datetime'] = pd.to_datetime(a['datetime'])
   val = a[a.datetime == datetime(d.year, d.month, d.day, d.hour, d.minute, 00)]
   ghi = val.iat[0, 2]
   return ghi
   




   
   
   
   
   







