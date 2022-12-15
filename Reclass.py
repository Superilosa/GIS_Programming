slp = QgsProject.instance().mapLayersByName('slope')[0]
out = r'C:\Users\iliko\Documents\GIS\Programireba\Raster\reclass.tif'

processing.run("native:reclassifybytable",{'INPUT_RASTER':slp,'RASTER_BAND':1,\
    'TABLE':[0,10,1,10,25,2,25,40,3,40,55,4],'NO_DATA':0,'RANGE_BOUNDARIES':2,'NODATA_FOR_MISSING':True,'DATA_TYPE':5,'OUTPUT':out})
    
iface.addRasterLayer(out)