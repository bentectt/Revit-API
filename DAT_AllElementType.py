# Enable Python support and load DesignScript library
import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('System')
from System.Collections.Generic import List

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

#Preparing input from dynamo to revit
link = UnwrapElement(IN[0])
category = UnwrapElement(IN[1])
#linkDoc = link.GetLinkDocument()

#elements = FilteredElementCollector(linkDoc).OfCategoryId(category.Id).WhereElementIsNotElementType()
result = []
#Create a genereic list for the elements
LinkName = []

#TransactionManager.Instance.EnsureInTransaction(doc)

for l in link :
	result2 = []
	linkDoc = l.GetLinkDocument()
	LinkName.append(l.Name)
	try:
		l = linkDoc.Settings.Categories
		for ll in l:
			result3 = []
			col = FilteredElementCollector(linkDoc).OfCategoryId(ll.Id).WhereElementIsElementType().ToElements()
			col2 = FilteredElementCollector(linkDoc).OfCategoryId(ll.Id).WhereElementIsElementType().ToElementIds()
			for e1, tId in zip(col, col2) :
				result4 = []
				tName = e1.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_NAME).AsString()
				fName = e1.FamilyName
				result3.append([tId, tName, fName, e1.Category.Name])
			result2.append(result3)
		result.append(result2)				
	except:
		result2.append("Error - Link is null")

	
#TransactionManager.Instance.TransactionTaskDone()

#All actions that makes changes to the Revit database needs to be inside a Transaction


OUT = result