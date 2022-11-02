riv = QgsProject.instance().mapLayersByName('Rivers')[0]

fields = riv.fields()
feats = riv.getFeatures()
DIST = 1000
out = r'C:\Users\iliko\Documents\GIS\Programireba\shp\bbuffer.shp'
writer = QgsVectorFileWriter(out,'UTF-8',fields,QgsWkbTypes.Polygon,riv.sourceCrs(),'ESRI Shapefile')

for i in feats:
    geo = i.geometry()
    buf = geo.buffer(DIST,10)
    i.setGeometry(buf)
    writer.addFeature(i)
del(writer)
    
iface.addVectorLayer(out,'','ogr')