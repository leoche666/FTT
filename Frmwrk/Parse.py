'''
@author: v-leoche
@summary: this class is designed for parse the xml
'''

from Type import *
import xml.sax

class ParseXMLTeamplate(xml.sax.ContentHandler):
    def __init__(self):pass

    def startDocument(self):
        self.varMap = VarMap()
        self.currentObject = []

    def endDocument(self):
        self.varMap.deal()
        pass
    
    def startElement(self, tag, attributes):                   
        if tag =="varmap":
            self.varMap.attributes = attributes._attrs
            self.varMap.deep = 0
            self.currentObject.append(self.varMap)
        elif tag=="var":
            var = Var()
            var.attributes = attributes._attrs
            var.attributes['LenofRecm'] = 0
            var.deep = len(self.currentObject)
            var.parent = self.currentObject[-1]
            self.currentObject[-1].child.append(var)
            self.currentObject.append(var)    
        elif tag=="fnc":
            fnc = Fnc()
            fnc.attributes = attributes._attrs
            fnc.deep = len(self.currentObject)
            fnc.parent = self.currentObject[-1]
            self.currentObject[-1].child.append(fnc)
            self.currentObject.append(fnc)
        elif tag=="ret":
            ret = Ret()
            ret.attributes = attributes._attrs
            ret.deep = len(self.currentObject)
            ret.parent = self.currentObject[-1]
            self.currentObject[-1].child.append(ret)
            self.currentObject.append(ret)               
        elif tag=="except":
            exp = Exp()
            exp.attributes = attributes._attrs
            exp.deep = len(self.currentObject)
            exp.parent = self.currentObject[-1]
            self.currentObject[-1].child.append(exp)
            self.currentObject.append(exp) 
        elif tag=="rec":
            rec = Rec()
            rec.attributes = attributes._attrs
            rec.deep = len(self.currentObject)
            rec.parent = self.currentObject[-1]
            self.currentObject[-1].child.append(rec)
            self.currentObject.append(rec)
        elif tag=="recm":
            recm = Recm()
            recm.attributes = attributes._attrs
            recm.deep = len(self.currentObject)
            recm.parent = self.currentObject[-1]
            self.currentObject[-1].child.append(recm)
            self.currentObject.append(recm)
        elif tag=="val":
            val = Val()
            val.attributes = attributes._attrs
            val.deep = len(self.currentObject)
            val.parent = self.currentObject[-1]
            self.currentObject[-1].child.append(val)
            self.currentObject.append(val)
        elif tag=="grp":
            grp = Grp()
            self.varMap.grp = grp
            grp.attributes = attributes._attrs
            grp.deep = len(self.currentObject)
            grp.parent = self.currentObject[-1]
            self.currentObject[-1].child.append(grp)
            self.currentObject.append(grp)
        elif tag=="snippet":
            snippet = Snippet()
            snippet.attributes = attributes._attrs
            snippet.deep = len(self.currentObject)
            snippet.parent = self.currentObject[-1]
            self.currentObject[-1].child.append(snippet)
            self.currentObject.append(snippet)
        elif tag=="snipref":
            snipref = Snipref()
            snipref.attributes = attributes._attrs
            snipref.deep = len(self.currentObject)
            snipref.parent = self.currentObject[-1]
            self.currentObject[-1].child.append(snipref)
            self.currentObject.append(snipref)
        elif tag=="varref":
            varref = Varref()
            varref.attributes = attributes._attrs
            varref.deep = len(self.currentObject)
            varref.parent = self.currentObject[-1]
            self.currentObject[-1].child.append(varref)
            self.currentObject.append(varref)
        else:
            raise Exception("Cann't support the tag : ",tag)
    
    def characters(self, content):
        elem = self.currentObject[-1]       
        if elem.__class__.__name__ == 'Fnc' \
        or elem.__class__.__name__ == 'Rec' \
        or elem.__class__.__name__ == 'Val' \
        or elem.__class__.__name__ == 'Ret' \
        or elem.__class__.__name__ == 'Exp':
            elem.value = content
                        
    def endElement(self, tag):
        elem = self.currentObject.pop()
        for child in elem.child:
            elem.len += 1
            if child.__class__.__name__ == 'Rec':
                elem.mapping.append([child.attributes['key'],child.value])
            elif child.__class__.__name__ == 'Recm':
                elem.mapping.append([child.attributes['key'],child.child])