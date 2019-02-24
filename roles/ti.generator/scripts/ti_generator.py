import sys
import os
import argparse
from string import Template
import pandas as pd
from src.extract import Extract_content
from src.generator import IT_generator_file

def main(configuration):
    content = dict({
                    'basic': configuration["content"],
                    'recursivity': configuration["recursivity"],
                    'port': configuration["port"]})

    generator_conf = dict({
                    "directory": configuration["directory"],
                    "file": configuration["file"],
                    "export": configuration["export"],
                    "type": '',
    })
    clean_content = Extract_content(content)
    content_data = clean_content.get_content()

    if content["basic"] or content["recursivity"]:
        generator_conf["type"] = "permissions"
        IT_generator_file(content_data, generator_conf).generate()
    elif content["port"]:
        generator_conf["type"] = "port"
        IT_generator_file(content_data, generator_conf).generate_port()

def parsarg():
    parser = argparse.ArgumentParser(description="ti_generator: Generator testinfra file for permissions tests.")
    parser.add_argument("-f", dest="file", help="File test name created for the content (-c)", type=str)
    parser.add_argument("-d", dest="directory", help="Directory for write tests files.)", type=str)
    parser.add_argument("-c", dest="content", help="Content for created test ('ls -adl' display).)", type=str)
    parser.add_argument("-r", dest="recursive_content", help="Content for created test ('ls -alR' display).)", type=str, default=False)
    parser.add_argument("-p", dest="port_content", help="Content for created test ('ss -ltnp' display).)", type=str)
    parser.add_argument("-a", dest="port_establish", help="Content for created test (add option '-a' to the ss content display).)", type=str)
    parser.add_argument("-e", dest="export", help="informations is formated to e readable(csv, xls).)", type=str, action='append')
    args = parser.parse_args()

    content = args.content
    return dict({"file": args.file, "directory": args.directory, "content" : content, 'recursivity': args.recursive_content, 'port': args.port_content, 'export': args.export})

if __name__ == '__main__':
    configuration = parsarg()
    main(configuration)
