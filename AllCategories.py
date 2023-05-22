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
categories = doc.Settings.Categories

model_cat = []
anno_cat = []
ana_cat = []
internal_cat = []

for c in categories:
	if c.CategoryType == CategoryType.Model:
		model_cat.append(Revit.Elements.Category.ById(c.Id.IntegerValue))
	elif c.CategoryType == CategoryType.Annotation:
		anno_cat.append(Revit.Elements.Category.ById(c.Id.IntegerValue))
	elif c.CategoryType == CategoryType.AnalyticalModel:
		ana_cat.append(Revit.Elements.Category.ById(c.Id.IntegerValue))
	elif c.CategoryType == CategoryType.Internal:
		internal_cat.append(Revit.Elements.Category.ById(c.Id.IntegerValue))
		

OUT = model_cat, anno_cat, ana_cat, internal_cat