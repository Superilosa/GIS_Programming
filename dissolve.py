#pMun = r'C:\Users\iliko\Documents\GIS\Programireba\shp\Municipalitys.shp'
#mun = iface.addVectorLayer(pMun,'','ogr')
mun = QgsProject.instance().mapLayersByName('Municipalitys')

out1 = r'C:\Users\iliko\Documents\GIS\Programireba\shp\GeoDiss.shp'
out2 = r'C:\Users\iliko\Documents\GIS\Programireba\shp\RegDiss.shp'

processing.run("native:dissolve",{'INPUT':mun,'OUTPUT':out1})
processing.run("native:dissolve",{'INPUT':mun,'FIELD':['Mxare'],'OUTPUT':out2})

iface.addVectorLayer(out1,'','ogr')
iface.addVectorLayer(out2,'','ogr')