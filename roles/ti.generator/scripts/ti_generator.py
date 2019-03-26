from src import parsarg
from src.extract import Extract_content_port, \
                        Extract_content_file, \
                        Extract_content_directory_recursive
from src.generator import IT_generator_content, \
                          IT_generator_port
from argparseGraph.argparseGraph import argparseGraph as agg

def main():
    configuration = parsarg()
    agG = agg("scenarios.yml", configuration)

    class_list_extract = [
                    Extract_content_file,
                    Extract_content_directory_recursive,
                    Extract_content_port
    ]
    class_list_generator = [
                    IT_generator_content,
                    IT_generator_content,
                    IT_generator_port
    ]

    scenario = agG.get_one()
    if type(scenario) is dict:
        return 0

    content = class_list_extract[scenario](configuration)
    content_data = content.get_content()

    generator = class_list_generator[scenario](content_data, configuration)
    generator.generate()

if __name__ == '__main__':
    main()
