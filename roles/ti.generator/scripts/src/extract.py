import re

class Extract_content_file:

    def __init__(self, configuration):
        self.__content = configuration.content.split("\n")
        self.__it_data = self._process_content()

    def get_content(self):
        return self.__it_data

    def _process_content(self):
        it_data = []
        for item in self.__content:
            tmp_dict = dict({})
            tmp_dict.update(self._get_file_name(item))
            tmp_dict.update(self._get_permission(item))
            tmp_dict.update(self._get_owner_group(item))
            it_data.append(tmp_dict)
        return it_data

    def _get_file_name(self, string):
        file_path = string.split(" ")[-1]
        return dict({'path': file_path})

    def _get_owner_group(self, string):
        owner, group = string.split(" ")[2:4]
        return dict({'owner': owner, 'group': group })

    def _permissions_to_number(self, perm):
        count = 0
        for l in perm:
            if 'r' in l:
                count += 4
            elif 'w' in l:
                count += 2
            elif 'x' in l:
                count += 1
        return count

    def _get_permission(self, data):
        type = data[0]
        user = self._permissions_to_number(data[1:4])
        group = self._permissions_to_number(data[4:7])
        other = self._permissions_to_number(data[7:10])
        full = "{}{}{}".format(user, group, other)

        permission_extract = dict({ 'permissions': {'full': full, 'user': user, 'group': group, 'other': other, 'type': type}})
        return permission_extract


class Extract_content_directory_recursive(Extract_content_file):

    def __init__(self, configuration):
        self.__content = configuration.recursive_content.split("\n")
        self.__it_data = self.__process_content_recursif()

    def get_content(self):
        return self.__it_data

    def __process_content_recursif(self):
        path = ''
        it_data = []
        for item in self.__content:
            tmp_dict = dict({})
            if item and '/' in item:
                path = item[:-1]
            elif item and "total" != item[:5] and '.' != item[-1]:
                if path and '/' == path[-1]:
                    tmp_dict.update(dict({'path': "{}{}".format(path, self._get_file_name(item)["path"])}))
                else:
                    tmp_dict.update(dict({'path': "{}/{}".format(path, self._get_file_name(item)["path"])}))
                tmp_dict.update(self._get_permission(item))
                tmp_dict.update(self._get_owner_group(item))
                it_data.append(tmp_dict)
        return it_data

class Extract_content_port:

    def __init__(self, configuration):
        self.__it_data = None
        self.__content = configuration.port_content.split("\n")
        self.__process_content_port()

    def get_content(self):
        return self.__it_data

    def __process_content_port(self):
        tmp_content = self.__content
        self.__it_data = []
        for i, item in enumerate(tmp_content):
            if i != 0 and item:
                tmp = re.sub(' +', ' ', item).split(' ')
                listen_address_port = re.sub(' +', ' ', item).split(' ')[3]
                users = re.sub(' +', ' ', item).split(' ')[-1]
                self.__it_data.append(dict({'address_port': listen_address_port, "users": users}))
