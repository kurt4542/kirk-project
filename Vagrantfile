# -*- mode: ruby -*-
# vi: set ft=ruby :

$post_script = <<SCRIPT
echo I am provisioning...
date > /etc/vagrant_provisioned_at
CHK_USER=`grep operation /etc/passwd`
if [[ -z $CHK_USER ]]; then
useradd -d /pang operation
mkdir -p ~operation/.ssh
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDjggePUaVLZxoUcvaAixJBPmRLpMIHW/4YQ8eerUFUW98WYvev1iEeu2t7C7XtTdotzVnlK/SvfCArxlf5XsOYctKQ/pwA1ehrrXAMZNNuQmOVvKgNney38VojA1g4/iUTn/1iVg84cuo/1i44qrgkjo815FPfNy+L63Z4Z9+wSPe70Bm5rV8r/55uJ/RbYhFRCIFjpcyztcjcyNWNJ0KJk8AvlOuRCRSqQnzkCxvs+4uNgoly5+zqZs8ewOWXB/I7rlOeGjX26WC90rh6JlsuVdbW9B51AFqS7FOFG1NVZYfE3e6SF9JM+AkFgsdLRgpzXpxL5RpRrX6eL7FP4NPh operation@jenkins" > ~operation/.ssh/authorized_keys
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCbdgtGuq4eLdpM51C6Jcpw+CtXV/aRh3sjMfy3rszLyFgLknZVyRc8YZBbggRZ85HBL4FGRnMPCgk1S8wNJzsMDpSANc/ngECnHoRppqijwHGnue9/ZiZo639RZ8ogC1MTyO60Z9MYzHmwUgo4Y0jxAMxYaulWkH3qHs33pg7W2NqaP1dpARTQno5aVOBb/bhOvuO8Tw7GxjKjpD28YRFv3E9RR8i119rKOx5F+hdUwEKGGg28TiE84vJZPMTknYbfCO4nJbprzWMXsWurEUsjGbKB3xsSxsRfLqNPMfpMKsjuTbATHcWr1aikqmQH6jOyEc3QuM0fOVDqL4ukVuWL ssh key for devops" >> ~operation/.ssh/authorized_keys
fi
echo "operation     ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers
chown -R operation.operation /pang
SCRIPT

Vagrant.configure(2) do |config|
  if (/cygwin|mswin|mingw|bccwin|wince|emx/ =~ RUBY_PLATFORM) != nil
    config.vm.synced_folder ".", "/vagrant", mount_options: ["dmode=700,fmode=600"]
  else
    config.vm.synced_folder ".", "/vagrant"
  end
  config.vm.define "jenkins_master01" do |jenkins|
    jenkins.vm.box = "ubuntu/trusty64"
    jenkins.vm.hostname = "jenkins-master01"
    jenkins.vm.network "forwarded_port", guest: 8080, host: 8080
    jenkins.vm.network "private_network", ip: "10.200.200.21"
    jenkins.vm.provision "shell", inline: $post_script
#       config.vm.provider "virtualbox" do |vb|
#        vb.customize ["modifyvm", :id, "--cpus", "2"]
#        vb.customize ["modifyvm", :id, "--memory", "4096"]
#       end
  end
  config.vm.define "jenkins_slave01" do |jenkins_slave|
    jenkins_slave.vm.box = "ubuntu/trusty64"
    jenkins_slave.vm.hostname = "jenkins-slave01"
    #jenkins_slave.vm.network "forwarded_port", guest: 5601, host: 5601
    jenkins_slave.vm.network "private_network", ip: "10.200.200.22"
#   jenkins_slave.vm.provision "shell", inline: $post_script
#       config.vm.provider "virtualbox" do |vb|
#        vb.customize ["modifyvm", :id, "--cpus", "2"]
#        vb.customize ["modifyvm", :id, "--memory", "4096"]
#       end
  end
end
