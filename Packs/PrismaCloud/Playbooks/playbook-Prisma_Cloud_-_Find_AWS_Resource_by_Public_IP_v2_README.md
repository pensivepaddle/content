Find AWS resources by Public IP using Prisma Cloud inventory.
Supported services: EC2, Network Load Balancer, ECS, Route53.


## Dependencies

This playbook uses the following sub-playbooks, integrations, and scripts.

### Sub-playbooks

This playbook does not use any sub-playbooks.

### Integrations

PrismaCloud v2

### Scripts

PrismaCloudAttribution

### Commands

prisma-cloud-config-search

## Playbook Inputs

---

| **Name** | **Description** | **Default Value** | **Required** |
| --- | --- | --- | --- |
| PublicIPAddress | Public IP address to look up. |  | Required |

## Playbook Outputs

---

| **Path** | **Description** | **Type** |
| --- | --- | --- |
| PrismaCloud.Attribution | Prisma Cloud attributed asset information. | unknown |

## Playbook Image

---

![Prisma Cloud - Find AWS Resource by Public IP v2](../doc_files/Prisma_Cloud_-_Find_AWS_Resource_by_Public_IP_v2.png)
