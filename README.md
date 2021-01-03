# osudb

A simple Python module to parse & serialize databases of [osu!](https://osu.ppy.sh), the rhythm game.

Version: 0.2  
Written by: KirkSuD  
Project started @ 2019/08/22  
Last update @ 2021/01/03  
Current found bugs: None

It is written according to [the osu! wiki page](https://osu.ppy.sh/help/wiki/osu!_File_Formats/Db_(file_format)).  
Currently, there are 4 databases: osu!.db, scores.db, collection.db, and presence.db.  
But presence.db is not described on the wiki page and is not supported.

Last test: Roughly tested @ 2021/01/03
 with osu!.db ver.20201102, collection.db ver.20200724, scores.db ver.20190828.

osu! directory path:  
Windows: %localappdata%/osu!  
Mac OSX: /Applications/osu!.app/Contents/Resources/drive_c/Program Files/osu!/

## Requirements

* Python, but this is only tested on Python 3.6.

## How to use

Just copy `osudb.py` to your working directory. Other files are not needed.

Then `import osudb`, run `osudb.parse_osu(file_path)` / `osudb.parse_collection(file_path)` /
 `osudb.parse_score(file_path)` / `osudb.serialize_osu(file_path, data)` / `osudb.serialize_collection(file_path, data)` /
 `osudb.serialize_score(file_path, data)`.

## How it works

It uses the Python module `struct` to parse primitive data.

## Related projects

* [OsuMusicPlayer](https://github.com/KirkSuD/OsuMusicPlayer) uses this to parse osu! databases and play music for you!

## TODO

* The code is really dirty... Clean it!
* Better python data <-> bytes mapping
* Better python data structure, OrderedDict maybe?
* Better error message to deal with DB struct changes
* Complete rewrite, using a format to represent the DB schema; so when DB struct changes, only changing the format is needed.
* Implement in [Kaitai Struct](https://kaitai.io/), cross-language parser looks really great!

## Bugs

Currently, there are no bugs found (all found ones are resolved).  
It parsed and serialized the DBs back to the original on my computer.

However, the databases' format may change, and the current parsing method may fail.  
If you find any bug, please inform me.

## Thanks to

* **huaji0353** for 20191106 version fix
* **Mrcubix** for finding boolean always True bug
