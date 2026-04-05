variable "aws_region" {
  description = "AWS region"
  default     = "eu-central-1"
}

variable "project_name" {
  description = "Project name prefix"
  default     = "url-shortener"
}

variable "table_name" {
  description = "DynamoDB table name"
  default     = "url-shortener-table"
}

