pMun = r'C:\Users\iliko\Documents\GIS\Programireba\shp\Municipalitys.shp'
mun = iface.addVectorLayer(pMun,'','ogr')

out = r'C:\Users\iliko\Documents\GIS\Programireba\shp\BufferDissolve.shp'

processing.run("native:buffer",{'INPUT':pMun,'DISTANCE':580,'DISSOLVE':True,'OUTPUT':out})

iface.addVectorLayer(out,'','ogr')