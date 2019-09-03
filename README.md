# osudb

A simple Python module to parse databases of [osu!](https://osu.ppy.sh), the rhythm game.

Version: 0.1  
Written by: KirkSuD  
Project started @ 2019/08/22  
Current found bugs: None

It is written according to [the osu! wiki page](https://osu.ppy.sh/help/wiki/osu!_File_Formats/Db_(file_format)).  
Currently, there are 4 databases: osu!.db, scores.db, collection.db, and presence.db.  
But presence.db is not described on the wiki page and is not supported.

Roughly tested @ 2019/08/22
 with osu!.db ver.20190816, collection.db ver.20190808, scores.db ver.20190524.

osu! directory path:  
Windows: %localappdata%/osu!  
Mac OSX: /Applications/osu!.app/Contents/Resources/drive_c/Program Files/osu!/

## Requirements

* Python, but this is only tested on Python 3.6.

## How to use

Just copy `osudb.py` to your working directory. Other files are not needed.

Then `import osudb`, run `osudb.parse_osu(file_path)` / `osudb.parse_collection(file_path)` /
 `osudb.parse_score(file_path)`.

## How it works

It uses the Python module `struct` to parse primitive data.

## Related projects

* [OsuMusicPlayer](https://github.com/KirkSuD/OsuMusicPlayer) uses this to parse osu! databases and play music for you!

## TODO

* The code is messy; clean it!

## Bugs

Currently, there are no bugs found.

However, the databases' format may change, and the current parsing method may fail.  
If you find any bug, please inform me.
