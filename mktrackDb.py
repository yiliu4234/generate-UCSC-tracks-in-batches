from optparse import OptionParser
import sys
usage = "usage: %prog [options] arg"
parser = OptionParser(usage)
parser.add_option("-n", "--track", dest="tname",
                      help="type value")
parser.add_option("-t", "--type", dest="dtype",
                      help="type value")
parser.add_option("-u", "--bigDataUrl", dest="DataUrl",
                      help="bigDataUrl value")
parser.add_option("-g", "--group", dest="group",
                      help="group value")
parser.add_option("-s", "--shortLabel", dest="shortLabel",
                      help="shortLabel value")
parser.add_option("-l", "--longLabel", dest="longLabel",
                      help="loneLabel value")
parser.add_option("-o", "--outputname", dest="output",
                      help="file name of trackDb")

(options,args)=parser.parse_args()
if __name__ == "__main__":
    if not(options.tname and options.dtype and options.DataUrl and options.group and options.shortLabel and options.longLabel and options.output):
        parser.print_help()
        sys.exit(0)
    f=open(options.output,'a')
    f.write("track "+options.tname+"\n")
    f.write("type "+options.dtype+"\n")
    f.write("bigDataUrl "+options.DataUrl+"\n")
    f.write("group "+options.group+"\n")
    f.write("shortLabel "+options.shortLabel+"\n")
    f.write("longLabel "+options.longLabel+"\n")
    f.write("visibility hide"+"\n")
    f.write("priority 1.00"+ "\n")
    f.write("autoScale on "+ "\n")
    f.write("yLineOnOff on"+"\n")
    f.write("windowingFunction mean"+"\n")
    f.write("\n")
    f.close()
