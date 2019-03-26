import argparse

def parsarg():
    parser = argparse.ArgumentParser(description="ti_generator: Generator testinfra file for permissions tests.")
    parser.add_argument("-f", dest="file", help="File test name created for the content (-c)", type=str)
    parser.add_argument("-d", dest="directory", help="Directory for write tests files.)", type=str, default="./")
    parser.add_argument("-c", dest="content", help="Content for created test ('ls -adl' display).)", type=str)
    parser.add_argument("-r", dest="recursive_content", help="Content for created test ('ls -alR' display).)", type=str)
    parser.add_argument("-p", dest="port_content", help="Content for created test ('ss -ltnp' display).)", type=str)
    # parser.add_argument("-a", dest="port_establish", help="Content for created test (add option '-a' to the ss content display).)", type=str)
    parser.add_argument("-e", dest="export", help="informations is formated to e readable(csv, xls).)", type=str, action='append')
    args = parser.parse_args()

    return args
