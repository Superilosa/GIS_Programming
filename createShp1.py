fn = r'C:\Users\iliko\Documents\GIS\Programireba\shp\tree.shp'

layerfield = QgsFields()
layerfield.append(QgsField('ID',QVariant.Int))
layerfield.append(QgsField('saxeoba',QVariant.String))
layerfield.append(QgsField('simaRle',QVariant.Double))

writer = QgsVectorFileWriter(fn,'UTF-8',layerfield,QgsWkbTypes.Point,QgsCoordinateReferenceSystem('EPSG:32638'),'ESRI Shapefile')

fc = QgsFeature()
fc.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(479505, 4616668)))
fc.setAttributes([1,'naZvi',20.7])
writer.addFeature(fc)

del(writer)