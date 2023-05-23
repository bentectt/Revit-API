#//Autor: Nited Prasong, November 2022 Made for Arup
#//contact: nited.prasong@gmail.com

#//Import mandatory module
import clr
import System
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
#//Get Current DBDocument (Current opened file)
doc = DocumentManager.Instance.CurrentDBDocument
#// Get Categories
cats = doc.Settings.Categories
#// Get BuiltInCategories
bics = System.Enum.GetValues(BuiltInCategory)
#// Create an empty list
CreatedSchedules = []
lst2 = []
#// Make input always a list
if isinstance(IN[0], list): categories = IN[0]
else: categories = [IN[0]]

Prefix = IN[1]
Suffix = IN[2]
fields = IN[3]

#// Start Transaction 
TransactionManager.Instance.EnsureInTransaction(doc)

#// Create Schedule for each category
for category in categories:
	fieldname = []
	temp = []
	CId = ElementId(category.Id)
	#// Create schedule
	schedules = ViewSchedule.CreateSchedule(doc, CId)
	CreatedSchedules.append(schedules)
	#//Set view name as Prefix + category name + Suffix
	param = schedules.GetParameters("View Name")
	param[0].Set(Prefix + str(category) + Suffix)
	SchDef = schedules.Definition
	SchFields = SchDef.GetSchedulableFields()
	#// Create a list of all parameters that can be scheduled
	for SchField in SchFields:
		AllFields = SchField.GetName(doc)
		fieldname.append(AllFields)
	
	#// Lookup the desired parameters respectively according to fields (IN[3])
	if fields is None:
		#// If fields IN[3] is empty use the list below
		fields = ["Workset","Family","Type","Count", "Level", "Reference Level", "Schedule Level"]
		#// Look up each parameters and add fields to each schedule respectively
		for fi in fields:
			indices = []
			for i, fName in enumerate(fieldname):
				if fName == fi:
					SchDef.AddField(SchFields[i])
					indices.append(i)
			temp.append(indices)	
		lst2.append(temp)
	else:
		for fi in fields:
			indices = []
			for i, fName in enumerate(fieldname):
				if fName == fi:
					SchDef.AddField(SchFields[i])
					indices.append(i)
			temp.append(indices)	
		lst2.append(temp)

#// Stop Transaction	
TransactionManager.Instance.TransactionTaskDone()

OUT = CreatedSchedules, lst2
