#
# Title:outputs.tf
# Description:
# Development Environment: Terraform v0.12.7
#
output "heeler_bucket" {
  value = aws_s3_bucket.heeler_bucket.id
}
#