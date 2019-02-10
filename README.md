# TI Generator

__summary__:
  - [Description](#description)
  - [Use it](#use-it)
  - [References](#references)


## Description

  This project aims to automate the creation of TestInfra scripts. It tests the files permissions for now, and more options will be added along the time.
  You can easily run it on your Production environment to fix configuration.
  Version 0.1.0

## Use it

  The generator is located in the role `ti.generator`, you have to set some targets file
  with the variable `TI_HOST_CONF`.

  Basic example:  
  __playbook.yml:__  
  ```yaml
  - hosts: v1
    vars:
     TI_HOST_CONF:
       - name: Fix prod
         file_name: testinfra-v1.py
         file_path: ti_result/
         ti_generator_target_folder:
           - /home/user_test1/
           - /home/user_test2/
       - name: Fix rec
         file_name: testinfra-v2.py
         file_path: ti_result/
         ti_generator_target_folder:
           - /home/user_test2/
           - /home/user_test3/
   roles:
     # - role: provisioner # provisioner create multiple user and folders tree.
     - role: ti.generator
  ```

  example with include vars:  
  __var/prod.yml:__
  ```yaml
    TI_HOST_CONF_tmp:
      - name: Fix prod
        file_name: testinfra-v1.py
        file_path: ti_result/
        ti_generator_target_folder:
          - /home/user_test1/
          - /home/user_test2/
  ```

  __var/rec.yml:__  
  ```yaml
  TI_HOST_CONF_tmp:
    - name: Fix rec
      file_name: testinfra-v2.py
      file_path: ti_result/
      ti_generator_target_folder:
        - /home/user_test2/
        - /home/user_test3/
  ```

  __playbook.yml:__  
  ```yaml
  - hosts: v1
    pre_tasks:
      - set_fact:
          TI_HOST_CONF: []

      - include_vars: vars/prod.yml

      - set_fact:
          TI_HOST_CONF: "{{TI_HOST_CONF}} +[ TI_HOST_CONF_tmp ]"

      - include_vars: vars/rec.yml

      - set_fact:
          TI_HOST_CONF: "{{TI_HOST_CONF}} +[ TI_HOST_CONF_tmp ]"
    roles:
      - role: ti.generator
  ```

  result for both examples :  
  __ti_result/testinfra-v1.py:__  
  ```py
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
      assert file_target.mode == 700

  # target: /home/user_test2/
  # assert on: ['file_exist', 'user', 'group', mode]
  def testinfra_v11(host):
      file_target = host.file('/home/user_test2/')
      assert file_target.user == 'user_test2'
      assert file_target.group == 'user_test2'
      assert file_target.mode == 700
  ```

  __ti_result/testinfra-v2.py:__  
  ```py

  #######################################
  # TestInfra generated by Ti-generator #
  #######################################
  # This tool is an open-source project on Github (https://github.com/kuty22/TI_Generator)


  # target: /home/user_test2/
  # assert on: ['file_exist', 'user', 'group', mode]
  def testinfra_v20(host):
      file_target = host.file('/home/user_test2/')
      assert file_target.user == 'user_test2'
      assert file_target.group == 'user_test2'
      assert file_target.mode == 700


  # target: /home/user_test3/
  # assert on: ['file_exist', 'user', 'group', mode]
  def testinfra_v21(host):
      file_target = host.file('/home/user_test3/')
      assert file_target.user == 'user_test3'
      assert file_target.group == 'user_test3'
      assert file_target.mode == 700

  ```

## References
- [Ansible website](https://www.ansible.com)
- [Molecule website](https://molecule.readthedocs.io/en/latest/)
- [TestInfra website](https://testinfra.readthedocs.io/en/latest/)
- [python3](https://docs.python.org/3.6/)
- Version = 0.1.0
