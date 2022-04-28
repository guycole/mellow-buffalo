#
# Title:s3.tf
# Description: deploy s3
# Development Environment: Terraform v0.12.18
#
# terraform cannot make a bucket name "gsc_core_v01.robobuzzer.com"
# Error: Error validating S3 bucket name: only lowercase alphanumeric characters and hyphens allowed in "gsc_core_v01.robobuzzer.com"
#
locals {
  heeler_bucket_name = "mellow-heeler-braingang-net"
}

resource "aws_s3_bucket" "heeler_bucket" {
  bucket = local.heeler_bucket_name

  tags = {
    Name        = "s3"
    Environment = terraform.workspace
  }
}