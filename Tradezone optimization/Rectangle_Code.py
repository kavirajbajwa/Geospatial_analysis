import numpy as np
from qgis.PyQt.QtCore import QVariant
from qgis.utils import iface
def polygonbuffer(outputFilename, bufferLength, polygonSides, irr_stretch):

 #Create New Layer
 #crs = iface.mapCanvas().mapSettings().destinationCrs().toWkt()
 newlayer = QgsVectorLayer('Polygon?crs=epsg:4326', 'polygon' , 'memory')
 new_provider = newlayer.dataProvider()
 
 # Add ids and coordinates fields
 fields = QgsFields()
 # fields.append(QgsField('longitude', QVariant.Double, '', 24, 20))
 # fields.append(QgsField('latitude', QVariant.Double, '', 24, 20))
 # new_provider.addAttributes(fields)
 
 #Select Active Layer
 layer = qgis.utils.iface.activeLayer()
 provider = layer.dataProvider()
 inFeat = QgsFeature()
 outFeat = QgsFeature()
 outFeat_1 = QgsFeature()
 inGeom = QgsGeometry()
 
 old_fields = layer.dataProvider().fields()
 newlayer.startEditing()
 new_provider.addAttributes(old_fields)
 newlayer.commitChanges()
 for inFeat in layer.getFeatures():
  point = inFeat.geometry().asPoint()
  inGeom = inFeat.geometry()
  #print(inFeat.attributes())
  for angle in np.linspace(0,2*np.pi,polygonSides, endpoint=False):
    if angle == 0:
      point_1 = QgsPointXY(point[0]+np.cos(angle)*bufferLength+irr_stretch, point[1]+np.sin(angle)*bufferLength)
    if angle == 1.0471975511965976:
      point_2 = QgsPointXY(point[0]+np.cos(angle)*bufferLength+irr_stretch, point[1]+np.sin(angle)*bufferLength)
    if angle == 2.0943951023931953:
      point_3 = QgsPointXY(point[0]+np.cos(angle)*bufferLength-irr_stretch, point[1]+np.sin(angle)*bufferLength)
    if angle == 3.141592653589793:
      point_4 = QgsPointXY(point[0]+np.cos(angle)*bufferLength-irr_stretch, point[1]+np.sin(angle)*bufferLength)
    if angle == 4.1887902047863905 :
      point_5 = QgsPointXY(point[0]+np.cos(angle)*bufferLength-irr_stretch, point[1]+np.sin(angle)*bufferLength)
    if angle == 5.235987755982988:
      point_6 = QgsPointXY(point[0]+np.cos(angle)*bufferLength+irr_stretch, point[1]+np.sin(angle)*bufferLength)
  pointttt= [ point_2, point_3, point_5,point_6]
  outFeat.setGeometry(QgsGeometry.fromPolygonXY([pointttt]))
 # outFeat.setAttributes([point[0],point[1]])
  outFeat.setAttributes(inFeat.attributes())
  new_provider.addFeatures([outFeat])
  newlayer.updateFields()
  newlayer.updateExtents()
 QgsProject.instance().addMapLayer(newlayer)
polygonbuffer("polygons.shp",0.0013486902283,6,0.000056482)
#polygonbuffer("polygons.shp",0.012,6,0.002715)