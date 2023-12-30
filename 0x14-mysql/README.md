# 0x14-mysql
The following instructions highlight how to install and configure `source-replica` replication in MySQL 5.7.* on a set of two servers.

## Step 1: Install MySQL 5.7
```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C
sudo apt update
sudo apt install mysql-server-5.7
```

## Step 2: Create the replication user and the user for the ALX augrader
Create user for allowing ALX checker to access the database:
```sql
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY '<password>'; (Replace with actual ALX checker password)
GRANT REPLICATION CLIENT ON . TO 'holberton_user'localhost'%';
```

Create a database named `tyrell_corp` with a table called `nexus6` and add at least one entry to it. Make sure that holberton_user has SELECT permissions on the table.
```sql
CREATE DATABASE tyrell_corp IF NOT EXISTS;
USE tyrell_corp;
CREATE TABLE nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    model VARCHAR(50),
    serial_number VARCHAR(20)
)
INSERT INTO nexus6 VALUES (1, 'Nexus 6', 'ABC123');

GRANT SELECT ON tyrell_corp.* TO 'holberton_user'@'localhost';
```

## Step 3: Set up the source server
Run the following command on the source server to allow the replica to connect to it:
`sudo ufw allow 3306`

Modify `/etc/mysql/mysql.conf.d/mysqld.cnf` on the source server to allow connections from the server IP address. The default behavior is to only allow connections from localhost.
- set `bind-address = <server_IP_address>`. Use the ip address of the source server.
- set `server-id = 1`. This set the unique ID used by MySQL internally to distinguish servers in the replication setup
- uncomment the line `log_bin	= /var/log/mysql/mysql-bin.log` to allow binary logging on the source
- uncomment `binlog_do_db  = <db_name>` and replace `db_name` with the name of the db to be replicated. Several databases can be specified by specifying this directive multiple times

Restart the mysql service:
`sudo systemctl restart mysql`

### Create a replication user
- log in to mysql:
`mysql -u root -p`
- Create the replica user and also allow the ALX autograder to inspect the users table for verifying if the replication user was set up correctly:
```sql
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
CREATE USER 'replica_user'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
FLUSH PRIVILEGES;
```
### Obtain the source instance’s current binary log coordinates:
- Close all the open tables in every database on your source instance and lock them:
```sql
FLUSH TABLES WITH READ LOCK;
SHOW MASTER STATUS;
```
The second line in the above command will display a table with the name of the binary log file and a position value, both of which should be noted for use in the replica.
- unlock the tables using the command: `UNLOCK TABLES;`
- create the database to be replicated it if does not exist

## Step 4: Set up the replica server
- open `/etc/mysql/mysql.conf.d/mysqld.cnf` and add the following lines:
  - `server-id = 2`
  - `log_bin =  <same value as corresponding line in source server>`
  - `binlog_do_db = <same value as corresponding line in source server>`
  - `relay-log = /var/log/mysql/mysql-relay-bin.log` (the location of the replica's relay log file)

Restart MySQL on the replica:
`sudo systemctl restart mysql`

Start the replication:
- open mysql on the replica
mysql -u root -p
- yype the following command. This can also be done more easily by pre-writing it in a text editor.
```sql
CHANGE MASTER TO
MASTER_HOST='source_server_ip',  -- the IP address of the source server
MASTER_USER='replica_user',      -- the name of the replica user
MASTER_PASSWORD='password',      -- the password of the replica user
MASTER_LOG_FILE='mysql-bin.000001',
MASTER_LOG_POS=899;              --the position obtained from the 'SHOW MASTER STATUS command' on the source
```
- activate the replica server: `START SLAVE;`

To view the replica status, type the following command in mysql on the replica server:
`SHOW SLAVE STATUS\G;`
To stop replication:
`STOP SLAVE;`
