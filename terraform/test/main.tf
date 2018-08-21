variable "profile" {
  default = "yanolja-dev-admin"
}

provider "aws" {
  region                  = "ap-northeast-2"
  profile                 = "${var.profile}"
}

variable "private_subnet_cidr" {
  default = "abc"
}

data "private_subnet_cidr" "private_subnet" {
  cidr = "${var.private_subnet_cidr}"
}

output "private_subnet_cidr" {
  value = "${data.private_subnet_cidr.private_subnet.cidr}"
}