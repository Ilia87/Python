import re

bad_chars = ['001_999_000013_0000`.`', "`;"]

with open('all tables.txt', mode='r', encoding='UTF8') as f:
    lines = f.readlines()
    text = ""
    for line in lines:
        l = line.replace("\n", "")
        text += l

    patterns = re.findall("(001_999_000013_0000.*?;)", text)
    #print("LENGTH %s" % (str(len(patterns))))
    for p in patterns:
        for i in bad_chars:
            p = p.replace(i, "")
        print(p)
    print(type(p))

