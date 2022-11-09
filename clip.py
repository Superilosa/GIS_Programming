mun = QgsProject.instance().mapLayersByName('Municipalitys')[0]
x = QgsProject.instance().mapLayersByName('Area_CLP')[0]

# Clip
out1 = r'C:\Users\iliko\Documents\GIS\Programireba\shp\mun_clip.shp'
processing.run("native:clip", {'INPUT':mun,'OVERLAY':x,'OUTPUT':out1})
iface.addVectorLayer(out1,'','ogr')

# Extract by extent
out2 = r'C:\Users\iliko\Documents\GIS\Programireba\shp\mun_extr_x.shp'
processing.run("native:extractbyextent", {'INPUT':mun,'EXTENT':x,'CLIP':False,'OUTPUT':out2})
iface.addVectorLayer(out2,'','ogr')

# Clip by extent
out3 = r'C:\Users\iliko\Documents\GIS\Programireba\shp\mun_clip_x.shp'
processing.run("gdal:clipvectorbyextent", {'INPUT':mun,'EXTENT':x,'OUTPUT':out3})
iface.addVectorLayer(out3,'','ogr')

# Extract by location
out4 = r'C:\Users\iliko\Documents\GIS\Programireba\shp\mun_extr_loc.shp'
processing.run("native:extractbylocation", {'INPUT':mun,'PREDICATE':0,'INTERSECT':x,'OUTPUT':out4})
iface.addVectorLayer(out4,'','ogr')