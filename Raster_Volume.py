dem = QgsProject.instance().mapLayersByName('dem_10')[0]
outhtml = r'C:\Users\iliko\Documents\GIS\Programireba\Statistics\demVol.html'
outTable = r'C:\Users\iliko\Documents\GIS\Programireba\Statistics\demVol.shp'

processing.run("native:rastersurfacevolume",{'INPUT':dem,'BAND':1,'LEVEL':0,'METHOD':0,'OUTPUT_HTML_FILE':outhtml,'OUTPUT_TABLE':outTable})