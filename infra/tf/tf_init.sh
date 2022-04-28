#
# Title:tf_init.sh
# Description: terraform setup
# Development Environment: OS X 10.13.6
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin:$HOME/local/bin; export PATH
#
export TF_LOG=TRACE
#
terraform init
#terraform init -backend-config=gsc_tf_backend
#
terraform workspace new mellow-buffalo-developer
terraform workspace new mellow-buffalo-production
#