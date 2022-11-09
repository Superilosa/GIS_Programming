aW = iface.addVectorLayer(r'C:\Users\iliko\Documents\GIS\Programireba\shp\aWara.shp','','ogr')
af = iface.addVectorLayer(r'C:\Users\iliko\Documents\GIS\Programireba\shp\afxazeTi.shp','','ogr')

out = r'C:\Users\iliko\Documents\GIS\Programireba\shp\merge.shp'

processing.run("native:mergevectorlayers", {'LAYERS':[aW,af],'OUTPUT':out})

iface.addVectorLayer(out,'','ogr')