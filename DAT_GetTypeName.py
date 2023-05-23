import clr

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
doc =  DocumentManager.Instance.CurrentDBDocument

clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

"""
Ensures input is a list object.
"""
def tolist(obj1):
	if hasattr(obj1,"__iter__"): return obj1
	else: return [obj1]

# The input Elements. We must UnwrapElement here to allow us to use Revit API...
elems = tolist(UnwrapElement(IN[0]))

# An empty array for storing results...
outList = []

# Loop through all given Elements...
for e in elems:
	
	# Get the Element Name...
	eName = e.Name
	
	# Since we are not sure what subclass of Element we will get, we should use something that all Element subclasses will have which is the Element.GetTypeId() method...
	tId = e.GetTypeId()
	
	# If this TypeId is invalid, then we put a null into the outList and skip the rest of the code in this loop...
	if tId == ElementId.InvalidElementId:
		outList.append(None)
		continue
	
	# Here we are getting the ElementType object from the Document...
	t = doc.GetElement(tId)
	
	# Now we get the Name. This is a parameter and we get it like this...
	tName = t.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_NAME).AsString()
	
	# For completeness, here is the Family Name which we get from ElementType.FamilyName property...
	fName = t.FamilyName
	
	# Put all these name values into an array and put into the outList...
	outList.append([eName, tName, fName])

# Return the outList to the graph...
OUT = outList