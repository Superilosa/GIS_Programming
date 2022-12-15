pSlp = r'C:\Users\iliko\Documents\GIS\Programireba\Raster\slope.tif'
slp = iface.addRasterLayer(pSlp)

stats = slp.dataProvider().bandStatistics(1,QgsRasterBandStats.All)
min = stats.minimumValue
a = 10
b = 25
c = 40
max = stats.maximumValue

CS = QgsColorRampShader()
CS.setColorRampType(QgsColorRampShader.Interpolated)

lst = [QgsColorRampShader.ColorRampItem(min,QColor(250,235,221)),\
    QgsColorRampShader.ColorRampItem(a,QColor(245,136,96)),\
    QgsColorRampShader.ColorRampItem(b,QColor('#cb1b4f')),\
    QgsColorRampShader.ColorRampItem(c,QColor('#611f53')),\
    QgsColorRampShader.ColorRampItem(max,QColor('#03051a'))]
    
CS.setColorRampItemList(lst)
shad = QgsRasterShader()
shad.setRasterShaderFunction(CS)

render = QgsSingleBandPseudoColorRenderer(slp.dataProvider(),1,shad)
slp.setRenderer(render)