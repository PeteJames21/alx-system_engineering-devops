# 0x0B. SSH
A series of tasks that demonstrate how to work with SSH keys

## 0-use_a_private_key
Write a Bash script that uses ssh to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`
Requirements:
- Only use ssh single-character flags
- You cannot use -l
- You do not need to handle the case of a private key protected by a passphrase

## 1-create_ssh_key_pair
Write a Bash script that creates an RSA key pair.
Requirements:
- Name of the created private key must be `school`
- Number of bits in the created key to be created `4096`
- The created key must be protected by the passphrase `betty`

## 2-ssh_config
Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:
- Your SSH client configuration must be configured to use the private key `~/.ssh/school`
- Your SSH client configuration must be configured to refuse to authenticate using a password

## 100-puppet_ssh_config.pp
Use Puppet to set up the configurations in `2-ssh_config`
