# About

Try Docker

# Install docker on Ubuntu using off-line package

Reference:

[Docker Document: Install on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

[Docker Document: Install Docker compose](https://docs.docker.com/compose/install/)

Download the correct version. (amd64 or check the CUP Architecture)

```
    sudo apt-get remove docker docker-engine docker.io containerd runc
    sudo dpkg -i docker-ce_20.10.6_3-0_ubuntu-xenial_amd64.deb
    sudo dpkg -i docker-ce-cli_20.10.6_3-0_ubuntu-xenial_amd64.deb
    sudo dpkg -i containerd.io_1.4.4-1_amd64.deb

	sudo usermod -aG docker $USER # then logout login

	service start docker

    # install docker-compose
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

Checker Docker Compose

```
    docker-compose --version
```
