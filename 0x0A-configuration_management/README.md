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
