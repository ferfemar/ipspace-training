# Homework 2 - Simple report

Simple multi-platform reporting framework created as second hands-on assigment. Virtual IOS (CSRv) router has been added to the test lab for this homework.

## Structure


* **getters** - tasks that retrieve and save info from devices
* **helpers** - useful scripts (e.g. Juniper OP table specs)
* **outputs** - output from devices saved in files
* **parsers** - tasks and templates used to process the information into reports
* **reports** - produced reports
* **run-getters.yml** - playbook tu run the getters
* **run-reports.yml**- playbook tu produce the reports

## Functions

The playbook `run-getters.yml` runs all the available getters and saves the information into files.

The playbook `run-reports.yml` reads the information from the files and produces all the available reports.

Advantage of this functional split is mainly faster development of new reports from information already gathered. Also it allows to reuse information across reports.

## Usage

Run all getters and then produce all reports:
```bash
ansible-playbook run-getters.yml
ansible-playbook run-reports.yml
```

It is possible to run just a single getter using variable "get", e.g.:
```bash
ansible-playbook run-getters.yml -e get=instances
ansible-playbook run-getters.yml -e get=napalm-facts
ansible-playbook run-getters.yml -e get=ccc-status
```

## Available getters

* **get-ccc-status** - gathers information about Circuit cross-connect (P2P L2 MPLS VPN) from Juniper devices  using juniper_junos_tables module. Works only for Junos as there is probably no counterpart for this VPN in  IOS.
* **get-instances** - gathers information about routing instances in the network using NAPALM
* **get-napalm-facts** - gathers basic device facts using NAPALM

## Available reports

* **report-ccc.csv** - report of all CCCs in the network and their status
* **report-instances.csv** - report of all routing instances in the network and their status
* **report-software-verions.csv** - report of software version information

## Known issues

* NAPALM module fails when retrieving network_instances when the target is Cisco router without any instance configured (Github issue: n/a )

* NAPALM module retrieves wrong information about Juniper instances in some cases (opened Github issues: [#1028](https://github.com/napalm-automation/napalm/issues/) [#1034](https://github.com/napalm-automation/napalm/issues/1034) )
