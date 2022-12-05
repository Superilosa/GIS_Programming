dem = r'C:\Users\iliko\Documents\GIS\Programireba\Raster\dem_10.tif'

## Slope
slp = r'C:\Users\iliko\Documents\GIS\Programireba\Raster\slope.tif'
processing.run("qgis:slope",{'INPUT':dem,'Z_FACTOR':1,'OUTPUT':slp})
iface.addRasterLayer(slp)
# Aspect
out = r'C:\Users\iliko\Documents\GIS\Programireba\Raster\aspect.tif'
processing.run("qgis:aspect",{'INPUT':dem,'OUTPUT':out}) # 'Z_FACTOR' : 1
iface.addRasterLayer(out)
# Hillshade
out = r'C:\Users\iliko\Documents\GIS\Programireba\Raster\hillshade.tif'
processing.run("qgis:hillshade",{'INPUT':dem,'AZIMUTH':249,'V_ANGLE':36,'OUTPUT':out}) # 'Z_FACTOR' : 1
iface.addRasterLayer(out)

# Contour
cont = r'C:\Users\iliko\Documents\GIS\Programireba\shp\contour.shp'
processing.run("gdal:contour",{'INPUT':dem,'BAND':1,'INTERVAL':8,'FIELD_NAME':'H',\
    'CREATE_3D':False,'IGNORE_NODATA':False,'OFFSET':0,'OUTPUT':cont})
iface.addVectorLayer(cont,'','ogr')
# Extent
ext = r'C:\Users\iliko\Documents\GIS\Programireba\shp\contour_extent.shp'
processing.run("native:polygonfromlayerextent",{'INPUT':cont,'ROUND_TO':0,'OUTPUT':ext})
ext = iface.addVectorLayer(ext,'','ogr')
# TIN
out = r'C:\Users\iliko\Documents\GIS\Programireba\Raster\contour_tin.tif'
processing.run("qgis:tininterpolation",{'INTERPOLATION_DATA':cont+'::~::0::~::1::~::1','METHOD':0,\
    'EXTENT':ext.extent(),'PIXEL_SIZE':100,'OUTPUT':out})
    #'INTERPOLATUION_DATA':(layer)::~::(1)::~::(2)::~::(3)
    # 1 - Use ZCoords (0 - don't use, 1 - use)
    # 2 - Field ID, -1 when using ZCoords
    # 3 - Type: 0-Point, 1-Structure Lines, 2-Break Lines
iface.addRasterLayer(out)

# Chart
hist = r'C:\Users\iliko\Documents\GIS\Programireba\Statistics\slope_hist.html'
processing.run("qgis:rasterlayerhistogram",{'INPUT':slp,'BAND':1,'BINS':5,'OUTPUT':hist})