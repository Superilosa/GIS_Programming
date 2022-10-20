pSetC = r'C:\Users\iliko\Documents\GIS\Programireba\shp\Settlments - Copy.shp'

#setC = iface.addVectorLayer(pSetC,'','ogr')
delf = setC.dataProvider().capabilities()
#Delete by index
if delf & QgsVectorDataProvider.DeleteFeatures:
    setC.dataProvider().deleteFeatures(list(range(5)))
    
#Delete by attributes
feats = setC.getFeatures()
dfeats = []
if delf & QgsVectorDataProvider.DeleteFeatures:
    for feat in feats:
        if feat['OBJECTID'] > 68 and feat['OBJECTID'] < 100 \
        or feat['NAMA1'] == "Zvare" or feat['NAMA1_REG'] == "Guria":
            dfeats.append(feat.id())
    setC.dataProvider().deleteFeatures(dfeats)
    setC.triggerRepaint()
    
#Delete fields
out = r'C:\Users\iliko\Documents\GIS\Programireba\shp\Settlments_NoName.shp'
processing.run("native:deletecolumn",{'INPUT':setC,'COLUMN':['NAMA1','NAMA1_REG'],'OUTPUT':out})
#iface.addVectorLayer(out,'','ogr')

#Delete duplicate by attribute
fil = r'C:\Users\iliko\Documents\GIS\Programireba\shp\Settlments_Filtered.shp'
dup = r'C:\Users\iliko\Documents\GIS\Programireba\shp\Settlments_Duplicates.shp'
processing.run("native:removeduplicatesbyattribute",{'INPUT':setC,'FIELDS':['NAMA1','NAMA1_REG'],'OUTPUT':fil,'DUPLICATES':dup})
#iface.addVectorLayer(fil,'','ogr')
#iface.addVectorLayer(dup,'','ogr')

#Delete duplicate geometries
filG = r'C:\Users\iliko\Documents\GIS\Programireba\shp\Settlments_GeoFilt.shp'
processing.run("native:deleteduplicategeometries",{'INPUT':setC,'OUTPUT':filG})
iface.addVectorLayer(filG,'','ogr')