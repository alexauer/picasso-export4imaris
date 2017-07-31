# picasso-export4imaris
Python script to convert and concatenate Picasso .hdf5 files to .txt multi-channel files for Imaris importing.

###	tl;dr
* Export4Imaris processes needs to be copied to the file path and ran via terminal.
* Run script: python export4imaris.py
* Every .hdf5 file in the folder will be processed and the localizations will be concatenated to "concat_export.txt" file for Imaris importing.
* Every .hdf5 file is handled as a channel. For infos see terminal prints.