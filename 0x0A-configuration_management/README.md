# 0x0A. Configuration management
This project consists of independent tasks that demonstrate the use of the Puppet in configuration management.
The Puppet manifest files are tested for compliance with the Puppet style guide using the `puppet-lint` package.

## 0-create_a_file.pp
Using Puppet, create a file in /tmp.

Requirements:
- File path is `/tmp/school`
- File permission is `0744`
- File owner is `www-data`
- File group is `www-data`
- File contains "I love Puppet"

## 1-install_a_package.pp
Using Puppet, install `flask` from `pip3`.

Requirements:
- Install `flask`
- Version must be `2.1.0`

## 2-execute_a_command.pp
Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:
- Must use the `exec` Puppet resource
- Must use `pkill`
