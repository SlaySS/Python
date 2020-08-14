# Create a new instance of the latest Ubuntu on an
# t2.micro node with an AWS Tag naming it "Ubuntu"

provider "aws" {
  region = "ap-southeast-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0007cf37783ff7e10"
  instance_type = "t2.micro"

 tags = {
    Name = "WEB_Ubuntu"
  }
}

resource "aws_vpc" "network_web" {
 cidr_block       = "192.168.10.0/24"
 instance_tenancy = "default"

 tags = {
   Name = "network_web"
 }
}

resource "aws_subnet" "aws_web_dmz" {
    cidr_block              = "192.168.10.0/29"
    vpc_id                  = aws_vpc.network_web.id
        tags = {
        Name            = "aws_web_dmz"
    }
}

resource "aws_security_group" "allow_web" {
  name        = "allow_web"
  description = "Allow WEB traffic"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
