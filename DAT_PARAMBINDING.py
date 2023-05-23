import clr
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

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

# The inputs to this node will be stored as a list in the IN variables.
element = UnwrapElement(IN[0])

lst = []
b = doc.ParameterBindings
for bb in b:
	c = bb.Categories
	lst.append(c)
# Assign your output to the OUT variable.
OUT = b, lst


