import sys
import os
import argparse
from string import Template
import pandas as pd
from src.extract import Extract_content
from src.generator import IT_generator_file

def main(configuration):
    clean_content = Extract_content(configuration["content"], configuration["recursivity"])
    IT_generator_file(clean_content.get_content(), configuration["directory"], configuration["file"], configuration["export"]).generate()

def parsarg():
    parser = argparse.ArgumentParser(description="ti_generator: Generator testinfra file for permissions tests.")

    parser.add_argument("-f", dest="file", help="File test name created for the content (-c)", type=str)
    parser.add_argument("-d", dest="directory", help="Directory for write tests files.)", type=str)
    parser.add_argument("-c", dest="content", help="Content for created test ('ls -adl' display).)", type=str)
    parser.add_argument("-r", dest="recursive_content", help="Content for created test ('ls -alR' display).)", type=str)
    parser.add_argument("-e", dest="export", help="informations is formated to e readable(csv, xls).)", type=str, action='append')
    args = parser.parse_args()


    if args.file is None and args.directory is None and args.content is None:
        print("Pass: empty parameters. (ti_generator.py)", file=sys.stderr)
        sys.exit(0)

    recursivity = False if args.content is not None else True
    content = args.content if args.content is not None else args.recursive_content
    return dict({"file": args.file, "directory": args.directory, "content" : content, 'recursivity': recursivity, 'export': args.export})

if __name__ == '__main__':
    configuration = parsarg()
    main(configuration)
