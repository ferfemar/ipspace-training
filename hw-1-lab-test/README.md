# Homework 1 - Build Your Own Network Automation Lab

Initial lab setup for Building Network Automation Solutions course

## Lab setup

* Community version of EVE-NG running on ESXi server
* At this point running 4 Juniper vMX routers
* All connected to one bridge which also connects to a Cloud object, connecting the topology to a Linux server (running on the same ESXi)
* UNL topology XML file attached

## Linux server setup

* Debian server
* Python, Ansible, Git and other software installed
* Hostname to IP mapping configured in the /etc/hosts file

## Ansible setup

* Ansible configuration in the user home folder (~/.ansible.cfg):

```ini
[defaults]
inventory = .ansible/hosts.yaml
host_key_checking = False
gathering = explicit
retry_files_save_path = ~/.ansible-retry
log_path= ~/.ansible/log/ansible.log
nocows = 1
```

* Ansible inventory in the user home folder (.ansible/hosts.yaml)

```yaml
all:
  children:
    junos:
      hosts:
        vMX1:
        vMX2:
        vMX3:
        vMX4:
      vars:
        ansible_user: root
        ansible_password: Juniper123
        ansible_network_os: junos
        ansible_connection: netconf
```

* Test playbook execution result:

```ansible
ferfecky@lablinux:~/ipspace-training/hw-1-lab-test$ ansible-playbook test-lab.yml 

PLAY [Playbook that verifies connection to lab devices] *************************************************************************************************************************************************************************************************************

TASK [Gather Junos facts using core module] *************************************************************************************************************************************************************************************************************************
ok: [vMX2]
ok: [vMX3]
ok: [vMX4]
ok: [vMX1]

TASK [Save to output to files for inspection] ***********************************************************************************************************************************************************************************************************************
changed: [vMX3]
changed: [vMX2]
changed: [vMX4]
changed: [vMX1]

PLAY RECAP **********************************************************************************************************************************************************************************************************************************************************
vMX1                       : ok=2    changed=1    unreachable=0    failed=0   
vMX2                       : ok=2    changed=1    unreachable=0    failed=0   
vMX3                       : ok=2    changed=1    unreachable=0    failed=0   
vMX4                       : ok=2    changed=1    unreachable=0    failed=0   

ferfecky@lablinux:~/ipspace-training/hw-1-lab-test$ 
```
