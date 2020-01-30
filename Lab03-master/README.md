CS421/621L Lab03

Setup Virtual Machine with Vagrant

Objectives:
•	Install and configure Ubuntu Server using Vagrant. Follow the instructions on page 182 (textbook) to install Vagrant.
•	Compare the difference with Ubuntu server setup (lecture 5)

Submission:

A screenshot of your Ubuntu terminal through SSH

** You should have installed the VirtualBox in lecture 5, if not please check the lecture notes and install it.

Install Vagrant
1. Go to https://www.vagrantup.com/downloads.html and download the latest version
2. Install the vagrant using default settings and restart your computer
3. Check from your command line/terminal the version of vagrant
		vagrant --version
 

4. Type vagrant and hit enter. It will display the basics of the vagrant



Set up a Vagrant file for your project (do this once for a project)
1.	 Open the Windows command prompt
2.	 Type mkdir vm1. This makes a folder made vm1.
3.	Type cd vm1. Now you are in vm1 folder.
4.	Type vagrant init. Once the command completes, a file named Vagrantfile is placed in your dir.
5.	Open Vagrantfile with a text editor such as Atom, Notepad++ …etc. Next, specify the version of Ubuntus’ VirtualBox, and how to configure and provision the VM. For this exercise, we will only configure two items:
a.	Specify a virtual box that you want instead of the base box specified in the origin Vagrantfile.
Change the line of config.vm.box="base" to the following block:
config.vm.define "ubuntutest" do |ubuntutest|  ubuntutest.vm.hostname = "ubuntutest"
ubuntutest.vm.box = "trusty-server"
ubuntutest.vm.box_url = "https://oss-binaries.phusionpassenger.com/vagrant/boxes/latest/ubuntu-14.04-amd64-vbox.box"
   end



b.	Create a forwarded port mapping which allows access to a specific port within the machine from a port on the host machine:
             config.vm.network "forwarded_port", guest: 80, host: 8080
  c. Save the file and exit the editor.
References for setting up a Vagrant file:
1) https://www.vagrantup.com/intro/getting-started/project_setup.html
2) https://www.vagrantup.com/intro/getting-started/boxes.html, the “Using a box” section
Up and SSH (do this whenever you need to start up the VM)
1.	In the Command Prompt, while still in dir vm1, Type vagrant up.
2.	Type vagrant ssh, OR, open putty from desktop. Set HostName: 127.0.0.1, Port: 2222. Click open.
3.	(For putty: Click yes. Log in with username vagrant and password vagrant.)
4.	You are now inside the virtual machine of Ubuntu. (save screenshot and submit it to canvas)
5.	 Check vagrant documentation for more information https://www.vagrantup.com/docs/index.html

