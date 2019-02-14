# TI Generator

__summary__:
  - [Description](#description)
  - [Use it](#use-it)
  - [References](#references)


## Description

  This project aims to automate the creation of TestInfra scripts. It tests the files permissions for now, and more options will be added along the time.
  You can easily run it on your Production environment to fix configuration.  
  Version 0.2.0

  __python requirement:__
  - xwlt
  - csv
  - pandas

## Use it

  The generator is located in the role `ti.generator`, you have to set some targets file
  with the variable `TI_HOST_CONF`.

  minimal playbook example:  
  __playbook.yml:__  
  ```yaml
  - hosts: v1
    vars:
    TI_HOST_CONF:
      - name: Fix prod #  configuration name
        file_name: testinfra-v1.py # test file generated nane
        file_path: ti_result/ # folder where the test file will be write on you host
        export_csv: false # export to csv file (the name is of the export file is the same than file_name with a different extension)
        export_xls: true # export to excel file (the name is of the export file is the same than file_name with a different extension)
        ti_generator_target_file: # file target for generate test file
          - /home/user_test1/
        ti_generator_target_recursive: # folder target with recursivity for generate test file
          - /home/user_test2/
          - /home/user_test3/
   roles:
     # - role: provisioner # provisioner create multiple user and folders tree.
     - role: ti.generator
  ```

  result:  
  __ti_result/testinfra-v1.py:__  
  ``` py
  #######################################
  # TestInfra generated by Ti-generator #
  #######################################
  # This tool is an open-source project on Github (https://github.com/kuty22/TI_Generator)


  # target: /home/user_test1/
  # assert on: ['file_exist', 'user', 'group', mode]
  def testinfra_v10(host):
      file_target = host.file('/home/user_test1/')
      assert file_target.user == 'user_test1'
      assert file_target.group == 'user_test1'
      assert file_target.mode == 0o700

  # target: /home/user_test2/
  # assert on: ['file_exist', 'user', 'group', mode]
  def testinfra_v11(host):
      file_target = host.file('/home/user_test2/')
      assert file_target.user == 'user_test2'
      assert file_target.group == 'user_test2'
      assert file_target.mode == 0o700

  ...
  ```

- [Ansible website](https://www.ansible.com)
- [Molecule website](https://molecule.readthedocs.io/en/latest/)
- [TestInfra website](https://testinfra.readthedocs.io/en/latest/)
- [python3](https://docs.python.org/3.6/)

| **version** | **description**                              |
|:-----------:|:-------------------------------------------- |
|   `0.1.0`   | generate testinfra script for specific file. |
|   `0.2.0`   | recursive folder and export (csv, xls)       |
|             |                                              |
