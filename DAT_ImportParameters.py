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

doc = DocumentManager.Instance.CurrentDBDocument


if isinstance(IN[0], list): elements = UnwrapElement(IN[0])
else: elements = [UnwrapElement(IN[0])]

if isinstance(IN[1], list): params = IN[1]
else: params = [IN[1]]

if isinstance(IN[2], list): data = IN[2]
else: data = [IN[2]]
#FILE_PATH = IN[1]
TransactionManager.Instance.EnsureInTransaction(doc)
lst = []
lst2 = []
lst3 = []
for element, param, dat in zip(elements, params, data):
	temp = []
	for da, p in zip(dat, param): # 1 param, 100 elements
		temp2 = []
		obso = []
		for ele, X in zip(element, da):
			try:
				e1 = ele.GetParameters(p)[0]
				eSt1 = e1.StorageType
				ss = str(eSt1)
				if ss == "ElementId":
					temp2.append("Not set")
					#temp2.append(e1.AsElementId())
				elif ss == "String" and X != None:
					#temp2.append(str(X))
					e1.Set(str(X))
					#temp2.append(e1.AsString())
				elif ss == "Integer":
					#temp2.append(int(X))
					e1.Set(int(X))
					#temp2.append(e1.AsInteger())
				elif ss == "Double":
					#temp2.append(float(X))
                    #eUnit = e1.DisplayUnitType
					#e = UnitUtils.ConvertToInternalUnits(float(X), eUnit)
					e1.Set(UnitUtils.ConvertToInternalUnits(float(X), eUnit))
					#temp2.append(e1.AsDouble())
				#temp.append(e1)
			except:
				eleT= ele.GetTypeId()
				eleType = doc.GetElement(eleT)
				e2 = eleType.GetParameters(p)[0]
				eSt2 = e2.StorageType
				ss2 = str(eSt2)
				e2Unit = e2.DisplayUnitType
				if ss2 == "ElementId":
					temp2.append("Not Set")
					#temp2.append(e2.AsElementId())
				elif ss2 == "String" and X != None:
					temp2.append(str(X))
					e2.Set(str(X))
					#temp2.append(e2.AsString())
				elif ss2 == "Integer":
					temp2.append(int(X))
					e2.Set(int(X))
					#temp2.append(e2.AsInteger())
				elif ss2 == "Double":
					temp2.append(float(X))
                   #eUnit = e2.DisplayUnitType
					#ee = UnitUtils.ConvertToInternalUnits(float(X), eUnit)
					e2.Set(UnitUtils.ConvertToInternalUnits(float(X), e2Unit))
                    
				    #temp2.append(e2.AsDouble())
			#e2 = eleType.GetParameters(p)
			#temp.append(e2)
		temp.append(temp2)
	lst.append(temp)
TransactionManager.Instance.TransactionTaskDone()			
			
	
	#header.append(ps)
	#ps.insert(0, "Id")
	
		
OUT = lst

# Work

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

doc = DocumentManager.Instance.CurrentDBDocument


if isinstance(IN[0], list): elements = UnwrapElement(IN[0])
else: elements = [UnwrapElement(IN[0])]

if isinstance(IN[1], list): params = IN[1]
else: params = [IN[1]]

if isinstance(IN[2], list): data = IN[2]
else: data = [IN[2]]

def ChangeUnit(param, number):
	pUnit = param.DisplayUnitType
	return UnitUtils.ConvertToInternalUnits(number, pUnit)

#FILE_PATH = IN[1]
#TransactionManager.Instance.EnsureInTransaction(doc)

T = Transaction(doc)
T.Start("START!!!")
lst = []
lst2 = []
lst3 = []
for element, param, dat in zip(elements, params, data):
	temp = []
	for da, p in zip(dat, param): # 1 param, 100 elements
		temp2 = []
		for ele, X in zip(element, da):
			eleType = doc.GetElement(ele.GetTypeId())
			if len(ele.GetParameters(p)) > 0:
				e1 = ele.GetParameters(p)[0]
				eBool = e1.UserModifiable
				eSt1 = e1.StorageType
				ss = str(eSt1)
				if ss == "ElementId" and eBool:
					temp2.append("Not set")
					#temp2.append(e1.AsElementId())
				elif ss == "String" and X != None and eBool:
					try:
						temp2.append(str(X))
						e1.Set(str(X))
					except:
						pass
					#temp2.append(e1.AsString())
				elif ss == "Integer" and eBool:
					temp2.append(int(X))
					e1.Set(int(X))
					#temp2.append(e1.AsInteger())
				elif ss == "Double" and eBool:
					eUnit = e1.DisplayUnitType
					temp2.append(float(X))
					#temp2.append(float(X))
					#e = UnitUtils.ConvertToInternalUnits(float(X), eUnit)
					e1.Set(UnitUtils.ConvertToInternalUnits(float(X), eUnit))
			elif len(eleType.GetParameters(p)) > 0:
				e2 = eleType.GetParameters(p)[0]
				eSt2 = e2.StorageType
				ss2 = str(eSt2)
				e2Bool = e2.UserModifiable
				if ss2 == "ElementId" and e2Bool:
					temp2.append("Not set")
				elif ss2 == "String" and X != None and e2Bool:
					e2.Set(str(X))
				elif ss2 == "Integer" and e2Bool:
					e2.Set(int(X))
				elif ss2 == "Double" and e2Bool:
					try:
						e2.Set(ChangeUnit(e2,float(X))
						temp2.append(float(X))
					except:
						pass	
		temp.append(temp2)	
	lst.append(temp)
	
#TransactionManager.Instance.TransactionTaskDone()			
T.Commit()			
	
	#header.append(ps)
	#ps.insert(0, "Id")
	
		
OUT = lst