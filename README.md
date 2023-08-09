# Spotify-Data-Splitter
Splits spotify data into files containing chunks


## Setup:
1. Install python 3.8 or higher from [here](https://www.python.org/downloads)
2. Install the script using `git clone https://github.com/SpaghettDev/Spotify-Data-Splitter` or click the green download button above
3. If you have installed using the green download button, extract the file somewhere
4. Open your preffered shell and `cd` into the directory containing the main.py file

## Usage:
```shell
python main.py "file" [split_number]
```
eg.:
```shell
python main.py "path/to/data.json"
```
or
```shell
python main.py "path/to/data.json" 2000
```

The files are named filename_splitX.ext, and are contained in the directory containing "data.json"!
