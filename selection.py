pMun = r'C:\Users\iliko\Documents\GIS\Programireba\shp\Municipalitys.shp'
pSet = r'C:\Users\iliko\Documents\GIS\Programireba\shp\Settlments.shp'
pSox = r'C:\Users\iliko\Documents\GIS\Programireba\shp\soxumi.shp'

#add new to project:
#mun = iface.addVectorLayer(pMun,'','ogr')
#set = iface.addVectorLayer(pSet,'','ogr')

#select from project:
mun = QgsProject.instance().mapLayersByName('Municipalitys')[0]
set = QgsProject.instance().mapLayersByName('Settlments')[0]

iface.mapCanvas().setSelectionColor(QColor('green'))
mun.selectAll()
mun.invertSelection()

processing.run("qgis:selectbyattribute",{'INPUT':mun,'FIELD':'Raioni','OPERATOR':0,'VALUE':'gagra','METHOD':0})
processing.run("qgis:selectbyattribute",{'INPUT':"Municipalitys",'FIELD':'Mosaxl_200','OPERATOR':2,'VALUE':50000,'METHOD':0})

mun.selectByExpression('"Mxare" = \'kaxeTi\'')
mun.selectByExpression('"Mosaxl_200" > 50000')

#select by location მთლიანი შრით
processing.run("native:selectbylocation",{'INPUT':set,'PREDICATE':[0],'INTERSECT':pSox,'METHOD':0})
#select by location არჩეული ობიექტებით
processing.run("native:selectbylocation",{'INPUT':"Settlments",'PREDICATE':[0],\
    'INTERSECT':QgsProcessingFeatureSourceDefinition("Municipalitys",selectedFeaturesOnly=True),\
    'METHOD':0})
    
out = r'C:\Users\iliko\Documents\GIS\Programireba\shp\Mun50000.shp'
writer = QgsVectorFileWriter.writeAsVectorFormat(mun,out,'UTF-8',driverName = 'ESRI Shapefile',onlySelected = True)
munNew = iface.addVectorLayer(out,'Municipalities_New','ogr')
del(writer)