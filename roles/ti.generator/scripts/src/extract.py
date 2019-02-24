import re

class Extract_content:

    def __init__(self, data): #contents, recursive_content):
        basic_content = data["basic"]
        recursive_content = data["recursivity"]
        port_content = data["port"]
        self.__it_data_port = None
        self.__it_data = []
        if port_content:
            self.__content = port_content.split("\n")
            self.__process_content_port()
        if basic_content:
            self.__content = basic_content.split("\n")
            self.__process_content()
        if recursive_content and type(recursive_content) == str:
            self.__content = recursive_content.split("\n")
            self.__process_content_recursif()


    def get_content(self):
        if self.__it_data_port:
            return self.__it_data_port
        return self.__it_data

    def __process_content_port(self):
        tmp_content = self.__content
        self.__it_data_port = []
        for i, item in enumerate(tmp_content):
            if i != 0 and item:
                tmp = re.sub(' +', ' ', item).split(' ')
                listen_address_port = re.sub(' +', ' ', item).split(' ')[3]
                users = re.sub(' +', ' ', item).split(' ')[-1]
                self.__it_data_port.append(dict({'address_port': listen_address_port, "users": users}))

    def __process_content(self):
        for item in self.__content:
            tmp_dict = dict({})
            tmp_dict.update(self.__get_file_name(item))
            tmp_dict.update(self.__get_permission(item))
            tmp_dict.update(self.__get_owner_group(item))
            self.__it_data.append(tmp_dict)

    def __process_content_recursif(self):
        path = ''
        for item in self.__content:
            tmp_dict = dict({})
            if item and '/' in item:
                path = item[:-1]
            elif item and "total" != item[:5] and '.' != item[-1]:
                if path and '/' == path[-1]:
                    tmp_dict.update(dict({'path': "{}{}".format(path, self.__get_file_name(item)["path"])}))
                else:
                    tmp_dict.update(dict({'path': "{}/{}".format(path, self.__get_file_name(item)["path"])}))
                tmp_dict.update(self.__get_permission(item))
                tmp_dict.update(self.__get_owner_group(item))
                self.__it_data.append(tmp_dict)

    def __get_file_name(self, string):
        file_path = string.split(" ")[-1]
        return dict({'path': file_path})

    def __get_owner_group(self, string):
        owner, group = string.split(" ")[2:4]
        return dict({'owner': owner, 'group': group })

    def __permissions_to_number(self, perm):
        count = 0
        for l in perm:
            if 'r' in l:
                count += 4
            elif 'w' in l:
                count += 2
            elif 'x' in l:
                count += 1
        return count

    def __get_permission(self, data):
        type = data[0]
        user = self.__permissions_to_number(data[1:4])
        group = self.__permissions_to_number(data[4:7])
        other = self.__permissions_to_number(data[7:10])
        full = "{}{}{}".format(user, group, other)

        permission_extract = dict({ 'permissions': {'full': full, 'user': user, 'group': group, 'other': other, 'type': type}})
        return permission_extract
