import json
import glob

dirIn = "submission.json/*"
fileOut = "submission.csv"


for pathIn in glob.glob(dirIn):
    print pathIn
    if "_SUCCESS" in pathIn:
        continue

    with open(fileOut, 'w') as fout:
        fout.write("id,cuisine\n")
        with open(pathIn) as fin:
            for line in fin:
                data = json.loads(line)
                fout.write("{0},{1}\n".format(data['id'], data['cuisine']))



