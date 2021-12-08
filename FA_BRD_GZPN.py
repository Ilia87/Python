import re

with open('FA_BRD_GZPN.txt', mode='r', encoding='UTF8') as f:
    lines = f.readlines()
    text = ""
    for line in lines:
        l = line.replace("\n", "");
        text += l

    patterns = re.findall("(FROM.*?;)", text);
    print("LENGTH %s" % (str(len(patterns))))
    for p in patterns:
        print(p)
