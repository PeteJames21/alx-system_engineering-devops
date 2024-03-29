# 0x0C. Web server
This directory contains a series of tasks that demonstrate how to work with a Nginx Web server. Each successive task builds on the previous until a complete (but rudimentary) web server has been developed.

**NOTE**: Tasks 1-4 show how to configure the server using Bash. These tasks could be accomplished more cleanly using Puppet or other configuration management tools. Bash is used here only for educational purposes.

## 0-transfer_file
Write a Bash script that transfers a file from our client to a server using `scp`:

Requirements:
- Accepts 4 parameters
  1. The path to the file to be transferred
  2. The IP of the server we want to transfer the file to
  3. The username scp connects with
  4. The path to the SSH private key that scp uses
- Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
- `scp` must transfer the file to the user home directory `~/`
- Strict host key checking must be disabled when using `scp`

## 1-install_nginx_web_server
Install Nginx on an ubuntu server and modify the root `/` to return "Hello World!"

## 2-setup_a_domain_name
Contains the domain name for the server hosting this project.

## 3-redirection
Configure Nginx to redirect users who visit the page /redirect_me

## 4-not_found_page_404
Configure Nginx to serve a page containing the string "Ceci n'est pas une page" when returning a 404 error code.
