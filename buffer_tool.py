riv = QgsProject.instance().mapLayersByName('Rivers')[0]
out = r'C:\Users\iliko\Documents\GIS\Programireba\shp\buffer.shp'

processing.run("native:buffer",{'INPUT':riv,'DISTANCE':500,'OUTPUT':out})

iface.addVectorLayer(out,'','ogr')