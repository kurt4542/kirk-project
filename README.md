Jenkins
============

Install Jenkins Mater
---------------------

```bash
vagrant up jenkins_master01

ansible-playbook -i inventory/hosts install_jenkins.yml -u operation
```

Install Jenkins Slave
---------------------

```bash
vagrant up jenkins_slave01

ansible-playbook -i inventory/hosts jenkins_slave.yml -u operation -e user_type=slave

```

Install Gitlab
--------------
```bash
ansible-playbook -i inventory/hosts install_gitlab.yml -u operation
```

