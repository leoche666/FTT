'''
Created on July 26, 2016
@author: v-leoche
'''
##############################################################################
#----------------------------------FTT data structure-------------------------
##############################################################################
class Base(object):
    attributes = {}
    value = ""
    deep = 0
    len = 0
    userObject = None
    child = []
    mapping = []
    parent = None
    whichChild = 0

    def __init__(cls):
        cls.child = []
        cls.mapping = []


    def reflect(cls):
        import importlib
        model = cls.attributes['cls']
        model_name=model[0:model.rfind('.')]
        _cls = model[model.rfind('.')+1:]
        reflection_model = importlib.import_module(model_name)
        cls.userObject = getattr(reflection_model, _cls)
        return cls.userObject

    def getValue(cls,key):
        nmapping = dict(cls.items)
        return nmapping.get(key)

    def putValue(cls,value):
        cls.value = value

    def __getitem__(cls,key):
        return cls.get(key)

    def leftChild(cls):
        if cls.hasLeftChild():
            return cls.parent.child[cls.whichChild - 1]

    def rightChild(cls):
        if cls.hasRightChild():
            return cls.parent.child[cls.whichChild + 1]

    def hasChild(cls):
        return len(cls.child)

    def hasLeftChild(cls):
        return cls.parent and len(cls.parent.child) and cls.whichChild - 1 >= 0 \
               and cls.parent.child[cls.whichChild - 1]

    def hasRightChild(cls):
        return cls.parent and len(cls.parent.child) and cls.whichChild + 1 <= len(cls.parent.child)-1 \
               and cls.parent.child[cls.whichChild + 1]

    def isSelf(cls):
        return cls.parent and cls.parent.child[cls.whichChild] == cls

    def isRoot(cls):
        return not cls.parent

    def isLeaf(cls):
        return not (len(cls.child))

class Node(type):
    def __new__(cls,name="Node",bases=(),dictionary={}):
        return type.__new__(cls, name, bases, dictionary)

    def __init__(cls, name, bases, dictionary):
        superclass = super(Node, cls)
        superclass.__init__(name, bases, dictionary)

class MultiSearchTree(object):
    len = 0
    child = []
    queue = []

    def searchNode(self,node):
        for child in node.child:
            self.queue.append(child)
            if child.hasChild():
                self.searchNode(child)

    def length(self):
        return self.len

    def __len__(self):
        return self.len

##############################################################################
#----------------------------------FTT data structure-------------------------
##############################################################################

#**************************************************************************************************************

##############################################################################
#----------------------------------FTT data abstraction-----------------------
##############################################################################
class Ret(Base):
    __metaclass__ = Node

class Exp(Base):
    __metaclass__ = Node

class Fnc(Base):
    __metaclass__ = Node

class Val(Base):
    __metaclass__ = Node

class Rec(Base):
    __metaclass__ = Node

class Recm(Base):
    __metaclass__ = Node

class VarPid(object):
    pid = 0
    items = []
    def setVarPid(cls,pid):
        for _k,_v in cls.mapping:
            if _v.__class__ is list :
                cls.items.append((_k,_v[pid].value))
            else:
                cls.items.append((_k,_v))

    def findSniprefs(cls):
        sniprefs = [child for child in cls.child if child.__class__.__name__ == 'Snipref']
        for snipref in sniprefs:
            yield snipref.ref.mapping

    def findSniprefById(cls,id):
        for child in cls.child:
            if child.__class__.__name__ == 'Snipref' and child.attributes.get('id') == id:
                return child.ref.mapping

class Var(Base,VarPid):
    __metaclass__ = Node

class Grp(Var):
    __metaclass__ = Node

class VarMapDeal(object):
    def dealPercentSymbol(cls,node):
        for i,(key,val) in enumerate(node.mapping):
            if val == "" or val is None or not (val[0] == '%' and val[-1] == '%'):
                continue
            else:
                for _k,_v in cls.grp.mapping:
                    if val[1:-1] == _k:
                        node.mapping[i][-1] = _v
                        continue

    def dealSnipref(cls,node):
        if node.__class__.__name__ == 'Snipref':
            for child in cls.child:
                if child.__class__.__name__ == 'Snippet' and child.attributes['id'] == node.attributes['id']:
                    node.ref = child
                    node.parent.mapping = node.parent.mapping + child.mapping
                    return

    def dealRecm(cls,node):
        if node.__class__.__name__ == 'Var':
            #add the property of 'full' and 'pict' in the feature
            if node.attributes.has_key('permutation'):
                if node.attributes['permutation']=='rows':
                    for key,val in node.mapping:
                        if val.__class__ is list:
                            node.attributes['LenofRecm'] = len(val)
                elif node.attributes['permutation']=='full':
                    pass
                elif node.attributes['permutation']=='pict':
                    pass

    def deal(cls):
        cls.searchNode(cls)
        for node in cls.queue:
            cls.dealPercentSymbol(node)
            cls.dealSnipref(node)
        for node in cls.queue:
            cls.dealRecm(node)

    def getVarByVid(cls,vid):
        for child in cls.child:
            if child.__class__.__name__ == 'Var' and child.attributes['vid'] == vid:
                return child
        else:
            return None

    def getVidBySet(cls,varSet):
        for child in cls.child:
            if child.__class__.__name__ == 'Var' and child.attributes['set'] == varSet:
                yield child.attributes['vid']

    def getAllVid(cls):
        for child in cls.child:
            if child.__class__.__name__ == 'Var':
                yield child.attributes['vid']

    def getAllVar(cls):
        for child in cls.child:
            if child.__class__.__name__ == 'Var':
                yield child


class VarMap(Base,VarMapDeal,MultiSearchTree,):
    __metaclass__ = Node


class Snippet(Base):
    __metaclass__ = Node

class SniprefBase(object):
    ref = None

class Snipref(Base,SniprefBase):
    __metaclass__ = Node

class Varref(Base):
    __metaclass__ = Node

##############################################################################
#----------------------------------FTT data abstraction-----------------------
##############################################################################


