from osgeo import gdal

dem = QgsProject.instance().mapLayersByName('dem_10')[0]
out = r'C:\Users\iliko\Documents\GIS\Programireba\Raster\calc_dem.tif'

ras = QgsRasterCalculatorEntry()
ras.ref = 'ras@1'
ras.raster = dem
ras.bandNumber = 1

calc = QgsRasterCalculator('(ras@1+100)/ABS(ras@1-100)',out,'GTiff',dem.extent(),dem.width(),dem.height(),[ras])
calc.processCalculation()
iface.addRasterLayer(out)