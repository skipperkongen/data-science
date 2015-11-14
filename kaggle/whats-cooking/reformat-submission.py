import json

pathIn = "submission.json/part-r-00000-9472bd00-68a1-4da3-a134-94e77efbfd37"
pathOut = "submission.csv"

with open(pathOut, 'w') as fout:
    fout.write("id,cuisine\n")
    with open(pathIn) as fin:
        for line in fin:
            data = json.loads(line)
            fout.write("{0},{1}\n".format(data['id'], data['cuisine']))



