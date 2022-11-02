riv = QgsProject.instance().mapLayersByName('Rivers')[0]

feats = riv.getFeatures()
l = []
for i in feats:
    l.append(i['Shape_Leng'])
l.sort(reverse=True)

processing.run("qgis:selectbyattribute",{'INPUT':riv,'FIELD':'Shape_Leng','OPERATOR':3,'VALUE':l[9],'METHOD':0})

out = r'C:\Users\iliko\Documents\GIS\Programireba\shp\RiversTop10.shp'
writer = QgsVectorFileWriter.writeAsVectorFormat(riv,out,'UTF-8',driverName='ESRI Shapefile',onlySelected=True)
riv2 = iface.addVectorLayer(out,'Rivers Longest 10','ogr')