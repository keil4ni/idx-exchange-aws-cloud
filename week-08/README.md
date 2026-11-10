# Week 8: Infrastructure as Code using Terraform

### Plan vs apply vs destroy

|    | What it does |
| -- | -- |
| plan    | Plan compares the config to the state file and to real AWS, then prints what it would add, change, or destroy. It doesn't change anything and is used as a safety check before anything is created. |
| apply   | Apply shows the plan, asks for confirmation, then creates/updates resources and records the results in the state file |
| destroy | Destroy deletes everything tracked in state (e.g VPC, subnets, route tables, NAT gateway, etc) |

### Why state matters

In Terraform, state matters because it maps each real world resource to your configuration and is used to determine what changes can be made (updates, deletion, etc) if needed. States are stored in a file called `terraform.tfstate` and backups are stored in `terraform.tfstate.backup`. They contain secret information so it would be recommended to not share states publicly to prevent the risk of data loss.