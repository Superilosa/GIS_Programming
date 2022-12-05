mun = QgsProject.instance().mapLayersByName('Municipalitys')[0]

out = r'C:\Users\iliko\Documents\GIS\Programireba\Statistics\mxare.html'
processing.run("qgis:barplot",{'INPUT':mun,'NAME_FIELD':'Mxare','VALUE_FIELD':'Mosaxl_200','OUTPUT':out})

out = r'C:\Users\iliko\Documents\GIS\Programireba\Statistics\raioni.html'
processing.run("qgis:barplot",{'INPUT':mun,'NAME_FIELD':'Raioni','VALUE_FIELD':'Mosaxl_200','OUTPUT':out})

out = r'C:\Users\iliko\Documents\GIS\Programireba\Statistics\polar.html'
processing.run("qgis:polarplot",{'INPUT':mun,'NAME_FIELD':'Mxare','VALUE_FIELD':'Mosaxl_200','OUTPUT':out})

out = r'C:\Users\iliko\Documents\GIS\Programireba\Statistics\scatter.html'
processing.run("qgis:vectorlayerscatterplot",{'INPUT':mun,'XFIELD':'Kaci','YFIELD':'Qali','OUTPUT':out})

out = r'C:\Users\iliko\Documents\GIS\Programireba\Statistics\scatter3d.html'
processing.run("qgis:scatter3dplot",{'INPUT':mun,'XFIELD':'Mosaxl_200','YFIELD':'Qali','ZFIELD':'Kaci','OUTPUT':out})