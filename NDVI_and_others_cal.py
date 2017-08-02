#Import modules arcpy 
import arcpy

#Import the environment settings and spatial analyst extension
from arcpy import env
from arcpy.sa import*

#Check out the Spatial Analyst extension
arcpy.CheckOutExtension("spatial")

#Add your workspace 
env.workspace = r'C:\Users\shoumik\Desktop\CVA TCT\8_23_2010\step6_ndvi_others'

#Set the input raster here 
input = r'C:\Users\shoumik\Desktop\CVA TCT\8_23_2010\step5b_clipped_images\2010.tif'

#Create raster directory and specify inputs. It references the input you specified above
result1 = "NDVI.tif"
result2 = "SAVI.tif"
result3 = "NDMI.tif"
result4 = "BI.tif"

#Landsat TM bands
Band1 = input + "\Band_1"
Band3 = input + "\Band_3"
Band4 = input + "\Band_4"
Band5 = input + "\Band_5"

#Note that arcpy.sa.Float returns a floating point raster
NDVI_result = arcpy.sa.Float(Raster(Band4) - Raster(Band3))/(Raster(Band4) + Raster(Band3))
print "Working"
SAVI_result = arcpy.sa.Float((1 + 0.5)*(Raster(Band4) - Raster(Band3)))/(Raster(Band4) + Raster(Band3) + 0.5)
print "Working"
NDMI_result = arcpy.sa.Float(Raster(Band4) - Raster(Band5))/(Raster(Band4) + Raster(Band5))
print "Working"
BI_result = arcpy.sa.Float(Raster(Band5) + Raster(Band3)) - (Raster(Band4) + Raster(Band1))/(Raster(Band5) + Raster(Band3)) + (Raster(Band4) + Raster(Band1))
print "Working"

#Saving output to result output you specified above
NDVI_result.save(result1)
SAVI_result.save(result2)
NDMI_result.save(result3)
BI_result.save(result4)
print "Successful"