pDem = r'C:\Users\iliko\Documents\GIS\Programireba\Raster\dem_10.tif'
dem = iface.addRasterLayer(pDem)
dp = dem.dataProvider()

# Global statistics
stats = dp.bandStatistics(1,QgsRasterBandStats.All)
print(stats.minimumValue)
print(stats.maximumValue)
print(stats.mean)
print(stats.range)
print(stats.sum)
print(stats.sumOfSquares)
# Pixel statistics
val, res = dp.sample(QgsPointXY(474517,4615243),1)
print(val,res)
val, res = dp.sample(QgsPointXY(503487,4610528),1)
print(val,res)


# TIN Array
from osgeo import gdal

ds = gdal.Open(dp.dataSourceUri())
tin_arr = ds.GetRasterBand(1).ReadAsArray()
print(tin_arr)
print(len(tin_arr))
print(len(tin_arr[0]))
print(tin_arr[1200][1200])