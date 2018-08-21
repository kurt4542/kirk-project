variable "port" { default = 80 }
variable "private_subnet_cidr" {
  default = "abc"
}

data "template_file" "init" {
  template = "$${foo}:${var.port}"

  vars {
    foo = "${count.index}"
  }
}

data "subnet_cidr" "private_subnet" {
  cidr = "${var.private_subnet_cidr}"
}

output "test" { value = "${data.template_file.init.rendered}" }
output "private_subnet_cidr" {
  value = "${data.subnet_cidr.private_subnet.cidr}"
}