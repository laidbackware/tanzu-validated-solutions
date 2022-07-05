### <a id="fwreq"> </a> Firewall Requirements
To prepare the firewall, you need to gather the following information:

1. NSX ALB Controller nodes and Cluster IP address.
2. NSX ALB Management Network CIDR.
3. TKG Management Network CIDR
4. TKG Shared Services Network CIDR
5. TKG Workload Network CIDR
6. TKG Cluster VIP Address Range
7. TKG Management VIP Address Range
8. TKG Workload VIP Address Range
9. Client Machine IP Address
10. Bootstrap machine IP Address
11. Harbor registry IP address
12. vCenter Server IP.
13. DNS server IP(s).
14. NTP Server(s).

|**Source**|**Destination**|**Protocol:Port**|**Description**|
| --- | --- | --- | --- |
|TKG Management and TKG Workload Networks|DNS Server<br>NTP Server|UDP:53<br>UDP:123|DNS Service <br>Time Synchronization|
|TKG Management and TKG Workload Networks|DHCP Server|UDP: 67, 68|Allows hosts to get DHCP addresses|
|TKG Management and TKG Workload Networks|vCenter IP|TCP:443|Allows components to access vCenter to create VMs and Storage Volumes|
|TKG Management, Shared service  and Workload Cluster CIDR|Harbor Registry|TCP:443|<p>Allows components to retrieve container images </p><p>This registry can be a local or a public image registry (projects.registry.vmware.com)</p>|
|TKG Management Cluster Network|TKG Cluster VIP Network |TCP:6443|For Management cluster to configure Workload Cluster|
|TKG Shared Service Cluster Network|TKG Cluster VIP Network|TCP:6443|Allow Shared cluster to register with management cluster|
|TKG Workload Cluster Network|TKG Cluster VIP Network|TCP:6443|Allow Workload cluster to register with management cluster|
|TKG Management, Shared service, and Workload Networks|AVI Controllers (NSX ALB Management Network)|TCP:443|Allow Avi Kubernetes Operator (AKO) and AKO Operator (AKOO) access to Avi Controller|
|AVI Controllers (NSX ALB Management Network)|vCenter and ESXi Hosts|TCP:443|Allow AVI to discover vCenter objects and deploy SEs as required|
|Admin network|Bootstrap VM|SSH:22|To deploy, manage  and configure TKG clusters|
|deny-all|any|any|deny|
|deny-all|any|any|deny|