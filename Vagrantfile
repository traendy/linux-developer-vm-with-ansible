
Vagrant.configure("2") do |config|

  # basebox
  config.vm.box = "tknerr/ubuntu2004-desktop"
  config.vm.box_version = "0.1.0"

  # override the basebox when testing (an approximation) with docker
  config.vm.provider :docker do |docker, override|
    override.vm.box = "tknerr/baseimage-ubuntu-20.04"
    override.vm.box_version = "1.0.0"
    # docker (in-docker) needs privileges for creating the docker socket
    docker.create_args = [ "--cap-add=NET_ADMIN" ]
  end

  # hostname
  config.vm.hostname = 'dev-vm'

  # virtualbox specific customizations
  config.vm.provider "virtualbox" do |vbox, override|
    vbox.cpus = 4
    vbox.memory = 4096
    vbox.customize ["modifyvm", :id, "--name", "Linux Developer VM"]
    vbox.customize ["modifyvm", :id, "--usb", "on"]
    vbox.customize ["modifyvm", :id, "--accelerate3d", "off"]
    vbox.customize ["modifyvm", :id, "--graphicscontroller", "vmsvga"]
    vbox.customize ["modifyvm", :id, "--vrde", "off"]
  end

  # vmware specific customizations
  config.vm.provider "vmware_desktop" do |vmware, override|
    vmware.vmx["displayname"] = "Linux Developer VM"
    vmware.vmx["numvcpus"] = "4"
    vmware.vmx["memsize"] = "4096"
    vmware.vmx["usb.present"] = "TRUE"
    vmware.vmx["usb.pcislotnumber"] = "33"
    vmware.vmx["usb_xhci.present"] = "TRUE"
  end

  # create new login user
  config.vm.provision "shell", privileged: true, path: 'scripts/setup-vm-user.sh',
    args: "user user"

  # run the actual update-vm provisioning script under the new login user
  config.vm.provision "shell", privileged: true, keep_color: true, run: "always", inline: <<-EOF
    sudo -i -u user ROLE_TAGS=#{ENV['ROLE_TAGS']} /vagrant/scripts/update-vm.sh #{ENV['UPDATE_VM_FLAGS']}
    EOF

end
