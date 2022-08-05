import json
from shutil import register_unpack_format
import pandas as pd
import array
data = []
i=0
with open('/Users/msidhu/Downloads/1657821828_14022.json') as f:
    for line in f:
        data.append(json.loads(line))
outfile =  open("/Users/msidhu/Desktop/output_file.json", "w")
for i in range(len(data)):
    policy = data[i]['result']
    sep = (policy['_raw'])
    parent = json.loads(sep)
    child = parent['content']['list']
    del (parent)["content"]
    def combine (parent, child):
        df = {'policy': "",'feed':""}
        df['policy'] = parent
        df['feed'] = child
        return (df)

    for j in range(len(child)):
        output = combine(parent, child[j])
        json.dump(output, outfile, indent=4)
        outfile.write('\n')






