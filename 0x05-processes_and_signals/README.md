# 0x05. Linux Processes and signals

## 0-what-is-my-pid
Write a Bash script that displays its own PID.

## 1-list_your_processes
Write a Bash script that displays a list of currently running processes.
- show all processes, for all users, including those which might not have a TTY
- display in a user-oriented format
- show process hierarchy

## 2-show_your_bash_pid
Without using `pgrep`, write a Bash script that displays lines containing the word `bash`, thus allowing you to easily get the PID of your Bash process.

## 3-show_your_bash_pid_made_easy
Without using `ps`, write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

## 4-to_infinity_and_beyond
Write a Bash script that displays To infinity and beyond indefinitely, with a sleep of 2 seconds in between each iteration.

## 5-dont_stop_me_now
Use the `kill` command to stop the `4-to_infinity_and_beyond` process

## 6-stop_me_if_you_can
Without using `kill` or `killall`, write a Bash script that stops the `4-to_infinity_and_beyond` process.

## 7-highlander
Write a Bash script that displays:
- `To infinity and beyond` indefinitely
- With a `sleep 2` in between each iteration
- `I am invincible!!!` when receiving a SIGTERM signal

## 8-beheaded_process
Write a Bash script that kills the `7-highlander` process.

## 100-process_and_pid_file
Write a Bash script that:
- Creates the file `/var/run/myscript.pid` containing its PID
- Displays `To infinity and beyond` indefinitely
- Displays `I hate the kill command` when receiving a `SIGTERM` signal
- Displays `Y U no love me?!` when receiving a `SIGINT` signal
- Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a `SIGQUIT` or `SIGTERM` signal

## 102-zombie.c
Write a C program that creates 5 zombie processes and then enters an inifinite while loop.
The zombie processes can be identified by executing the compiled C program and then running the following command:
```
ps aux | grep -e 'Z+.*<defunct>'
```
