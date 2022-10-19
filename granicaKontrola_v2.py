import arcpy
import os

aprx = arcpy.mp.ArcGISProject("CURRENT")

nrPlanu = arcpy.GetParameterAsText(0)
grPrzy = arcpy.GetParameterAsText(1)

aprxFile = aprx.filePath
folder = aprx.homeFolder
arcpy.env.workspace = r"{}\brg_mpzp.gdb".format(folder)
arcpy.env.overwriteOutput = True
workspace = arcpy.env.workspace
mpzpMap = aprx.listMaps(f"{nrPlanu}_MPZP")[0]
grProc = mpzpMap.listLayers("GRANICA")[0]

with arcpy.EnvManager(XYResolution="0.0001 Unknown", MTolerance=0.0001, outputCoordinateSystem='PROJCS["ETRS_1989_Poland_CS2000_Zone_6",GEOGCS["GCS_ETRS_1989",DATUM["D_ETRS_1989",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",6500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",18.0],PARAMETER["Scale_Factor",0.999923],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]', XYTolerance="0.0001 Unknown", MResolution=0.0001):
    arcpy.analysis.SymDiff(grPrzy, grProc, r"{}\GRANICA_ROZNICE".format(workspace), "ALL", None)

mpzpMap.addDataFromPath(r"{}\GRANICA_ROZNICE".format(workspace))
grR = mpzpMap.listLayers("GRANICA_ROZNICE")[0]
                                     
arcpy.AddMessage("Sprawdź tabelę atrybutów dla warstwy GRANICA_ROZNICA!")


#aprx.save()
