# generate-UCSC-tracks-in-batches
There are many files to be writen in tracks in a project.We can write them all once with mktrackDb.py</br>
* usage
```Options:
  -h, --help            show this help message and exit
  -n TNAME, --track=TNAME
                        track value
  -t DTYPE, --type=DTYPE
                        type value
  -u DATAURL, --bigDataUrl=DATAURL
                        bigDataUrl value
  -g GROUP, --group=GROUP
                        group value
  -s SHORTLABEL, --shortLabel=SHORTLABEL
                        shortLabel value
  -l LONGLABEL, --longLabel=LONGLABEL
                        loneLabel value
  -o OUTPUT, --outputname=OUTPUT
                        file name of trackDb
```
* for example
```
for i in `ls | grep .bw` ;do ./mktrackDb.py -n $i -t bigWig -u $i -g "dalian Mecical University" -s `echo $i | awk -F "." '{print $1}'` -l `echo $i | awk -F "." '{print $1}' ` -o test_trackDb.txt ;echo $i;done
```
