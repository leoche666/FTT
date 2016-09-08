import os
import sys
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
import settings
from Frmwrk.Thread import ThreadConfig
root=os.path.abspath(r"..")
sys.path.append(root)
import argparse

parser = argparse.ArgumentParser("ftt")
parser.add_argument('-runserver',help='set runserver item true',action='store_true',dest="runserver")
parser.add_argument('-x','-xml', help='which xml will run',dest="xml",type=str)
parser.add_argument('-v','-vid', help='run the specified case in specified xml',dest="vid",type=str)
parser.add_argument('-s','-set', help='run the cases which have the same set value in specified xml',dest="set",type=str)
parser.add_argument('-a','-all', help='run the all cases in specified xml',dest="all",action='store_true')
parser.add_argument('-log', help='store the log in specified place',dest="log",type=str)
parser.add_argument('-html', help='store the html in specified place',dest="html",type=str)
parser.add_argument('-c','-case', help='print the cases in specified xml',dest="cases",action='store_true')
parser.add_argument('-ve','-version', help="print the ftt version and information about author",dest="version",action='store_true')
parser.add_argument('-common', help='set common item true',action='store_true',dest="common")
parser.add_argument('-ad','-address', help='which object will be runned',dest="address",type=str)
parser.add_argument('-g','-args', help='some arguments in running',dest="args",type=str)
args = parser.parse_args()

def deal():
    #the xml path
    if args.xml:
        args.xml = os.path.join(settings.resource, args.xml + '.xml')
    else:
        args.xml = settings.OPTIONS['xml']

    #the option
    opt = None
    tOption = filter(lambda t:t[1],[("v:",args.vid),("s:",args.set),("a:",args.all)])
    if len(tOption) > 1:
        print "-v|-vid -s|-set -a|-all must set one"
        sys.exit(2)
    elif len(tOption) == 1:
        opt = "" if tOption[0][0] == "a:" else tOption[0][0] + tOption[0][1]

    #the log path
    if not args.log:
        args.log = settings.OPTIONS['log']

    #the html path
    if not args.html:
        args.html = settings.OPTIONS['html']

    return opt

def start():
    if args.runserver:
        opt = deal()
        if args.version:
            print '''FTT Version 1.0.0\nFTT design by LeonChen with python 2.7.11\nEmail            | Author\n-----------------|---------\n673965587@qq.com |Leon Chen\nDesigned in 2016-07-20
                  '''
        elif args.cases:
            import importlib
            moudle = importlib.import_module("Frmwrk.Control")
            varmap = getattr(moudle, "Config").load_xml(args.xml)
            for var in varmap.getAllVar():
                print "vid:%s set:%s dsc:%s" % (var.attributes.get('vid'),var.attributes.get('set'),var.attributes.get('dsc'))
        else:
            kwargs = {'settings': settings, 'xml':args.xml, 'opt':opt, 'log':args.log, 'html':args.html}
            ThreadConfig()(**kwargs)
    elif args.common:
        import importlib
        address = args.address
        model_name = address[:address.rfind('.')]
        mimport = address[address.rfind('.')+1:]
        reflection_model = importlib.import_module(model_name)
        instance = getattr(reflection_model, mimport)
        #the arguments in running
        if not args.args:
            args.args = []
        else:
            args.args = eval(args.args)
        instance(*args.args)

if __name__ == '__main__':
    start()
