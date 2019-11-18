# Homework 4 - Deploy Network Services From a Data Model

Building on data models from exercise # 3. Playbooks deploying service provider infrastructure plus IPv4 (Internet) and L3 VPNv4 services. 

## Data models

* fabric.yml - describes nodes, links, internet transits, ASN and route reflector role
  * nodes - list of nodes in the netwok, id of every node is used to construct router id
  * transits - list of sessions to other AS, eBGP is assumed
  * fabric - list of connections inside the network
  * network - definition of network ASN and route reflector designation
* services-ipv4.yml - IPv4 Internet services
  * dictionary of routers, each router has a list of Internet services provided with necessary parameters
* services-vpnv4.yml - L3 MPLS VPN services
  * dictionary of customers, each customer has a RD and locations dict which in turn contains routers and list of locations for each
* nodes.yml - auto-generated from fabric data model using playbook pb-fabric-to-nodes.yml
  
## Playbooks

* pb-fabric-to-nodes.yml - transforms fabric.yml data model into device specific nodes.yml data model
* pb-configs.yml - generates infrastructure device configurations from the nodes.yml data model
* pb-deploy.yml - deploys the infrastructure configuration data model to the devices
* service-ipv4/pb-configs.yml - generates IPV4 Internet service configs
* service-ipv4/pb-deploy-ipv4.yml - deploys IPV4 Internet service configs
* service-vpnv4/pb-configs.yml - generates L3 MPLS VPN service configs
* service-vpnv4/pb-deploy-vpnv4.yml - deploys L3 MPLS VPN service configs
* validations/pb-validate-infra.yml - runs infrastructure validations

## Things to be improved / todo list

* Multiplatform support for services (Cisco)
* Make the configs more real world - routing protocols etc.
* Validations: LLDP, BGP, enhanced ISIS
