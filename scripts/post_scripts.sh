#!/usr/bin/env bash

echo "provisioning is starting"
date > /etc/vagrant_provisioned_at

CHK_USER=`grep operation /etc/passwd`
if [[ -z $CHK_USER ]]; then
    useradd -d /pang operation
    mkdir -p ~operation/.ssh
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDjggePUaVLZxoUcvaAixJBPmRLpMIHW/4YQ8eerUFUW98WYvev1iEeu2t7C7XtTdotzVnlK/SvfCArxlf5XsOYctKQ/pwA1ehrrXAMZNNuQmOVvKgNney38VojA1g4/iUTn/1iVg84cuo/1i44qrgkjo815FPfNy+L63Z4Z9+wSPe70Bm5rV8r/55uJ/RbYhFRCIFjpcyztcjcyNWNJ0KJk8AvlOuRCRSqQnzkCxvs+4uNgoly5+zqZs8ewOWXB/I7rlOeGjX26WC90rh6JlsuVdbW9B51AFqS7FOFG1NVZYfE3e6SF9JM+AkFgsdLRgpzXpxL5RpRrX6eL7FP4NPh operation@jenkins" > ~operation/.ssh/authorized_keys
fi

echo "operation     ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers

chown -R operation.operation /pang

echo ""
echo "Provisioning is completed..."