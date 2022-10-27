pRiv = r'C:\Users\iliko\Documents\GIS\Programireba\shp\Rivers.shp'
pMun = r'C:\Users\iliko\Documents\GIS\Programireba\shp\Municipalitys.shp'

#riv = iface.addVectorLayer(pRiv,'','ogr')
#mun = iface.addVectorLayer(pMun,'','ogr')
riv = QgsProject.instance().mapLayersByName('Rivers')[0]
mun = QgsProject.instance().mapLayersByName('Municipalitys')[0]


# Add column
dRiv = riv.dataProvider()
dRiv.addAttributes([QgsField('Type',QVariant.String),QgsField('Type_Eng',QVariant.String)])
riv.updateFields()


# Update fields with constant expression
cxRiv = QgsExpressionContext()
cxRiv.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(riv))
with edit(riv):
    for i in riv.getFeatures():
        cxRiv.setFeature(i)
        i['Type'] = 'mdinare'
        i['Type_Eng'] = 'River'
        riv.updateFeature(i)

        
# Update fields with calculation
dRiv.addAttributes([QgsField('Len_M',QVariant.Double)])
riv.updateFields()
lenX = QgsExpression('$length')
lenX.prepare(cxRiv)#(Optional for better performance)
with edit(riv):
    for i in riv.getFeatures():
        cxRiv.setFeature(i)
        i['Len_M'] = lenX.evaluate(cxRiv)
        riv.updateFeature(i)
        

# Chain of expressions
dMun = mun.dataProvider()
dMun.addAttributes([QgsField('area',QVariant.Double),QgsField('area_km',QVariant.Double),QgsField('simWidrove',QVariant.Double)])
mun.updateFields()
cxMun = QgsExpressionContext()
cxMun.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(mun))
x1 = QgsExpression('$area')
x2 = QgsExpression('"area"/1000000')
x3 = QgsExpression('"Mosaxl_200"/area_km')
with edit(mun):
    for i in mun.getFeatures():
        cxMun.setFeature(i)
        i['area'] = x1.evaluate(cxMun)
        mun.updateFeature(i)
with edit(mun):
    for i in mun.getFeatures():
        cxMun.setFeature(i)
        i['area_km'] = x2.evaluate(cxMun)
        mun.updateFeature(i)
with edit(mun):
    for i in mun.getFeatures():
        cxMun.setFeature(i)
        i['simWidrove'] = x3.evaluate(cxMun)
        mun.updateFeature(i)