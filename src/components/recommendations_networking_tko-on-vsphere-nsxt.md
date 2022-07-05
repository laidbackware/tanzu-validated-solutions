### Network Recommendations
The key network recommendations for a production-grade Tanzu Kubernetes Grid deployment with NSX-T Data Center Networking are as follows:

|**Decision ID**|**Design Decision**|**Design Justification**|**Design Implications**|
| --- | --- | --- | --- |
|TKO-NET-001|Configure ESXi transport nodes directly on VDS, not on N-VDS.|NSX ALB does not detect the logical segments created in vCenter Cloud if you configure the hosts with N-VDS.|NSX ALB does not support using NSX-T Cloud for deploying Tanzu Kubernetes clusters.|
|TKO-NET-002|Use separate logical segments for management cluster, shared services cluster, workload clusters, and all VIP/data networks.|To have a flexible firewall and security policies.|Sharing the same network for multiple clusters can complicate firewall rules creation.|
|TKO-NET-003|Configure DHCP  for each TKG cluster network.|Tanzu Kubernetes Grid does not support static IP address assignments for Kubernetes VM components.|IP address pool can be used for the TKG clusters in absence of the DHCP.|
|TKO-NET-004|Use NSX-T for configuring DHCP|NSX-T provides DHCP service on logical segments.|For a simpler configuration, make use of the DHCP local server to provide DHCP services for required segments.|
|TKO-NET-005|(Optional) Spread segments across multiple tier-1 gateways.|Configure the segments across multiple tier-1 gateway for tenant isolation.|When the segments are spread across multiple tier-1 gateway, required firewall rules need to be configured on each tier-1 gateway.|