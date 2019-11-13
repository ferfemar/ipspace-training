# Homework 3 - Data Models: Create a Service Data Model

First data model exercise (homework 3) solution. Data models describing simple service provider infrastructure plus IPv4 (Internet) and L3 VPNv4 services. A set of playbooks for data model transformations, configuration generation and simple deployment to lab devices for verification.

This solution will be improved upon in the following homeworks.

## Data models

* fabric.yml - describes nodes, links, internet transits, ASN and route reflector role
* nodes.yml - generated from fabric data model using playbook pb-fabric-to-nodes.yml
* services-ipv4.yml - IPv4 Internet services
* services-vpnv4.yml - L3 MPLS VPN services

## Playbooks

* pb-fabric-to-nodes.yml - transforms fabric.yml data model into device specific nodes.yml data model
* pb-configs.yml - generates infrastructure device configurations from the nodes.yml data model
* pb-deploy.yml - deploys the infrastructure configuration data model to the devices
* service-ipv4/pb-configs.yml - generates IPV4 Internet service configs
* service-ipv4/pb-deploy-ipv4.yml - deploys IPV4 Internet service configs