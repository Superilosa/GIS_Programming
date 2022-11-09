pSet = r'C:\Users\iliko\Documents\GIS\Programireba\shp\Settlments.shp'
pMun = r'C:\Users\iliko\Documents\GIS\Programireba\shp\Municipalitys.shp'
out = r'C:\Users\iliko\Documents\GIS\Programireba\shp\Settlents_clipped.shp'
set = iface.addVectorLayer(pSet,'','ogr')
mun = iface.addVectorLayer(pMun,'','ogr')

mun.selectByExpression('"Mxare" = \'raWa-leCxumi\' or "Mxare" = \'aWara\'')

#QgsProcessingFeatureSourceDefinition-ში მისამართით უნდა გადავცეთ შრე, თორემ არ მუშაობს
processing.run("native:extractbylocation", {'INPUT':set,'PREDICATE':[0],\
    'INTERSECT':QgsProcessingFeatureSourceDefinition(pMun,selectedFeaturesOnly=True),'OUTPUT':out})
    
iface.addVectorLayer(out,'','ogr')