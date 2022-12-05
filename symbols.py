pRiv = r'C:\Users\iliko\Documents\GIS\Programireba\shp\Rivers.shp'
riv = iface.addVectorLayer(pRiv,'','ogr')

# Simple symbol
sym = QgsLineSymbol.createSimple({'color':'blue'})
riv.renderer().setSymbol(sym)
riv.triggerRepaint()
sym = QgsLineSymbol.createSimple({'line_style':'dash','color':'#2887ed'})
riv.renderer().setSymbol(sym)
riv.triggerRepaint()


# Graduated
from qgis.PyQt import QtGui

LF = 'Shape_Leng'
sym_list = []
OPA = 25

minval = 25
maxval = 25000
lab = 'short'
col = QtGui.QColor('#0300e7')
sym = QgsSymbol.defaultSymbol(riv.geometryType())
sym.setColor(col)
sym.setOpacity(OPA)
#sym = QgsLineSymbol.createSimple({'color':'#0300e7'})
rang = QgsRendererRange(minval,maxval,sym,lab)
sym_list.append(rang)

minval = 25001
maxval = 316602
lab = 'long'
col = QtGui.QColor('#f80090')
sym = QgsSymbol.defaultSymbol(riv.geometryType())
sym.setColor(col)
sym.setOpacity(OPA)
#sym = QgsLineSymbol.createSimple({'color':'#f80090'})
rang = QgsRendererRange(minval,maxval,sym,lab)
sym_list.append(rang)

groupRenderer = QgsGraduatedSymbolRenderer('',sym_list)
groupRenderer.setMode(QgsGraduatedSymbolRenderer.EqualInterval)
groupRenderer.setClassAttribute(LF)
riv.setRenderer(groupRenderer)
riv.triggerRepaint()