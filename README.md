# About

A simple script to translate all string values inside one JSON file.

# Important

If the file was not fully translated, google blocked your IP, due to excessive requests. You can try to translate the JSON file in batches or change the script to use the google translate API for example.

# Installing

To install the program, you need to run:

```
$ python3 setup.py install
```

After installation, you can run the program, using for example:

```
$ translate-json-cli -i input-path/example.json -o output-path/example-translated.json
```

To get the help, you can use the argument -h or --help, for example:

```
$ translate-json-cli -h
usage: translate-json-cli [-h] -i path -o path [-s SRC] [-d DEST]

A program to translate a JSON file.

optional arguments:
  -h, --help            show this help message and exit
  -i path, --ifile path
                        JSON file path to be translated.
  -o path, --ofile path
                        translated JSON file path to be saved.
  -s SRC, --src SRC     the source language you want to translate. (Default: auto)
  -d DEST, --dest DEST  the destination language you want to translate. (Default: en)
```

# Only running the script

If you only want to run the script, first of all, you will need to install all dependencies necessary you can use pip3 to do that:

```
$ pip3 install .
```

Now run the main.py script using python3, like that:

```
$ python3 translate_json/main.py -i example.json -o example-translated.json
```
