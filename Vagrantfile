# Simple masterless salt setup to test docker and django

Vagrant.configure(2) do |config|
  config.vm.box = "fedora/23-cloud-base"

  config.vm.provision :salt do |salt|
    salt.minion_config = "minion"
    salt.run_highstate = true

    # allow dockerng to be used
    salt.install_type = "git"
    salt.install_args = "v2015.8.7"
  end
end
