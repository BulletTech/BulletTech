---
template: overrides/blogs.html
tags:
  - docker
---

# Teaching You to Successfully Run Docker on Win10 System

!!! info
    Author: Tina, Published on 2021-11-13, Reading time: about 5 minutes, WeChat article link: [:fontawesome-solid-link:](https://mp.weixin.qq.com/s/8B9ye55zpWCCVTA4g4fLQQ)

## 1 Introduction

In the previous article, [First Experience with Docker](https://mp.weixin.qq.com/s/gfO5BiK9fqRtWf8rjP8mPA), we introduced some basic concepts and common commands of Docker. However, because Docker creates resource isolation mechanisms on Linux systems, it cannot be directly run on Windows systems. This time, we will take 4 minutes to introduce how to run Docker on Win10 system.

## 2 Download Docker

Users can choose [Mac](https://docs.docker.com/desktop/mac/install/'Install docker in Mac') or [Windows](https://docs.docker.com/desktop/windows/install/#install-docker-desktop-on-windows'Install docker in Windows') on the Docker official website according to their own system. Because Docker can be directly run after installation on the Mac system, we will not go into details here.

After installing Docker and registering a personal account, double-click to start it, and you will find that it is not as smooth as you thought. The error message is shown in the figure below:

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/failed.jpg" width="500" />
  <figcaption> Failed to start Docker </figcaption>
</figure>

This is because Docker cannot be directly run on Windows systems, and a Linux virtual machine (VM) in the Windows system needs to be created to build the underlying dependencies for Docker's normal operation. Although the [official document](https://docs.docker.com/desktop/windows/install/#wsl-2-backend 'Installation of WSL2') provides two solutions, hyper-V and WSL2, WSL2 is an upgraded version of WSL1 based on hpyer-V. Its functions and installation methods are simple and convenient. Therefore, the author chooses the WSL2 backend method to run Docker.

## 3 Install WSL2

WSL, Windows Subsystem for Linux, means the Linux subsystem under Windows system. You can install WSL2 for Docker in just three steps in the system. Please note that WSL2 currently supports Windows10 2004 and above.

### 3.1 Enable WSL2

First, open the `Powershell` command prompt and run the command to view all subsystems on the Internet, then select the system you want to install. Here we will choose Ubuntu for installation.

```shell
## View the list
wsl --list --online
## Install Linux distribution
wsl --install -d Ubuntu
```

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/terminal-1.jpg" width="500" />
  <figcaption> View WSL list </figcaption>
</figure>

After the installation is successful, the result will prompt you to create a UNIX username and password:

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/create-account.jpg" width="500" />
  <figcaption> Create a username and password </figcaption>
</figure>

You will notice that the logo in the upper left corner of the command prompt has changed to Ubuntu.

### 3.2 Install update package

After successful installation, you also need to download the Linux installation update package. The specific operation needs to refer to the [Microsoft](https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package 'Install update package') official document and select the appropriate update package according to your system version.

### 3.3 Set the default version

Open the command prompt and set WSL2 as the default version of the Linux distribution:

```shell
wsl --set-default-version 2
```

### 3.4 Set WSL configuration file

Because the default configuration of WSL will occupy up to 80% of the computer's memory space, to avoid this situation, it is better to set the configuration file.

Press `Windows + R`, search for `%UserProfile%` to open the user's resource management file path, create and customize the `.wslconfig` document. Open it with Notepad and enter relevant parameters for configuration:

```
[wsl2]
# Set the memory to 2G, mainly for service docker
memory=2GB
# The maximum number of CPUs used
processors=2
# Do not set the swap space allocated by the WSL2 virtual machine
swap=0
# Allow forwarding of WSL2 ports to the host
localhostForwarding=true
```

## 4 Check Docker settings

After successfully installing the Linux distribution, you also need to set some basic parameters about WSL2 in Docker desktop to ensure the successful operation of Docker.

First, you need to select the engine based on WSL2 in the general settings, as shown below:

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/docker-1.png" width="500" />
  <figcaption> Based on WSL2 engine </figcaption>
</figure>

Secondly, you need to set up the integration of WSL in the resources. This operation helps you integrate and compose parts when you have multiple WSLs.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/docker-2.png" width="500" />
  <figcaption> Set WSL integrated resources </figcaption>
</figure>

Finally, restart Docker desktop, and you will see the successfully started interface.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/img/success.jpg" width="500" />
  <figcaption> Successful interface </figcaption>
</figure>

## 5 Conclusion

For some software to run successfully in the system, some prerequisites are indeed needed. Whether you are referring to specific official documents or searching for some experience posts to avoid thunder, after successfully installing and using them, you will find that the construction of these environments is a once-and-for-all thing. Try running Docker in your Windows system now! We will continue to share our learning experience with Docker, so stay tuned.

I hope this sharing can help you. Welcome to leave a message for discussion.

<figure>
  <img src="https://cdn.jsdelivr.net/gh/BulletTech2021/Pics/2021-6-14/1623639526512-1080P%20(Full%20HD)%20-%20Tail%20Pic.png" width="500" />
</figure>