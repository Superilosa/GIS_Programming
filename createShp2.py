fn = r'C:\Users\iliko\Documents\GIS\Programireba\shp\turtle.shp'

#შექმნა
layerfield = QgsFields()
layerfield.append(QgsField('ID',QVariant.Int))
layerfield.append(QgsField('Name',QVariant.String))
layerfield.append(QgsField('X',QVariant.Double))
layerfield.append(QgsField('Y',QVariant.Double))

writer = QgsVectorFileWriter(fn,'UTF-8',layerfield,QgsWkbTypes.Point,QgsCoordinateReferenceSystem('EPSG:32638'),'ESRI Shapefile')

XY = [(479413, 4616447), (479400, 4616450), (479390, 4616479), (479388, 4616516), (479405, 4616560),
        (479429, 4616581), (479574, 4616625), (479632, 4616630), (479688, 4616614), (479735, 4616587),
        (479749, 4616577), (479754, 4616562), (479753, 4616542), (479741, 4616529), (479690, 4616500)]
for i in XY:
    fc = QgsFeature()
    fc.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(i[0],i[1])))
    fc.setAttributes([XY.index(i),'Turtle_Lake',i[0],i[1]])
    writer.addFeature(fc)
    
del(writer)
iface.addVectorLayer(fn,'turtle_point','ogr')

#წერტილიდან ხაზში კონვერტაცია
line = r'C:\Users\iliko\Documents\GIS\Programireba\shp\turtle_line.shp'
processing.run("native:pointstopath",{'INPUT':fn,'CLOSE_PATH':True,'ORDER_EXPRESSION':'"ID"','OUTPUT':line})
iface.addVectorLayer(line,'','ogr')

#ხაზიდან პოლიგონში კონვერტაცია
pol = r'C:\Users\iliko\Documents\GIS\Programireba\shp\turtle_pol.shp'
processing.run("qgis:linestopolygons",{'INPUT':line,'OUTPUT':pol})
iface.addVectorLayer(pol,'turtle_polygon','ogr')