# The Command Challenge
The [command challenge](https://cmdchallenge.com/) is a game that helps practice Bash skills. The objective of this project is to complete the first 27 tasks in the challenge and upload screenshots of proof of completion of each successive 9 tasks. A drawing of an animal is automatically displayed at the top of the screen as each task is completed.

The screenshots are uploaded to the ALX sandbox environment via `sftp` using the following steps:
1. `cd` into the local directory where the screenshots are saved
2. Connect to the ALX sandbox using the SFTP URL:
```
sftp <user>@<host>
```
3. Enter the password when prompted
4. `cd` into the `root` directory and create the `alx-system_engineering-devops/command_line_for_the_win/` using the `mkdir` command. The `-p` flag does not work in `sftp`, so the two directories are created using two successive `mkdir` commands
5. Copy each screenshot to the remote directory using the command:
```
put file-name.png
```
The file will be saved with the same name in the remote directory.
