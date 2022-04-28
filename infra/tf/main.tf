#
# Title:main.tf
# Description: main
# Development Environment: Terraform v0.12.18
#
provider "aws" {
  profile = lookup({
    braingang  = "terraform_braingang",
  }, terraform.workspace, "default")

  region = var.aws_region
}

terraform {
  backend "s3" {
    bucket               = "terraform.braingang.net"
    encrypt              = true
    key                  = "terraform.tfstate"
    profile              = "terraform_braingang"
    region               = "us-west-2"
    workspace_key_prefix = "mellow"
  }
}
