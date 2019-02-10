
#######################################
# TestInfra generated by Ti-generator #
#######################################
# This tool is an open-source project on Github ()


# target: /home/user_test1/
# assert on: ['file_exist', 'user', 'group', mode]
def testinfra_v10(host):
    file_target = host.file("/home/user_test1/")
    assert file_target.user == user_test1
    assert file_target.group == user_test1
    assert file_target.mode == 700


# target: /home/user_test2/
# assert on: ['file_exist', 'user', 'group', mode]
def testinfra_v11(host):
    file_target = host.file("/home/user_test2/")
    assert file_target.user == user_test2
    assert file_target.group == user_test2
    assert file_target.mode == 700
