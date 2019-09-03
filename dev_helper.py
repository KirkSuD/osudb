#-*-coding:utf-8;-*-

"""
Development helper script.

A database parser for osu! databases.

Wiki: https://osu.ppy.sh/help/wiki/osu!_File_Formats/Db_(file_format)
Currently, 4 databases: osu!.db, scores.db, collection.db, and presence.db.
presence.db is not described in the wiki page and will not be parsed.

Windows: %localappdata%/osu!
Mac OSX: /Applications/osu!.app/Contents/Resources/drive_c/Program Files/osu!/
"""

### small helper functions for development ###
def get_lines():
    res = []
    while True:
        s = input()
        if not s: return res
        res.append(s)
def parse_wiki(s):
    return [[j.strip() for j in i.split("\t", maxsplit=1)] for i in s]

## for development
import pprint
wiki = parse_wiki(get_lines())
pprint.pprint(wiki)
print([i[0] for i in wiki])
#for i in sorted(list(set([i[0] for i in wiki]))):
#    print('elif data_type == "%s":' % i)
