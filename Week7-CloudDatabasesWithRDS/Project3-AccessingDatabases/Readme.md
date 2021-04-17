# Accessing Databases

1. In AWS, go to the deployed database
2. To connect to the database, you can do the following:
    - https://dev.mysql.com/downloads/workbench/
    - https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-install.html
3. For Mac, I installed the mysql shell
4. In the database in AWS..
    - Obtain the endpoint `cloudskills-mysql-db.cgmyv9zj836w.us-east-1.rds.amazonaws.com`
    - Port `3306`

5. From the terminal, enter the following:
    - `brew install mysql-client`
    - Then, add the mysql-client binary directory to your PATH: `echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.bash_profile`
    - Finally, reload your bash profile: `source ~/.bash_profile`
    - Then run: `mysql -h cloudskills-mysql-db.cgmyv9zj836w.us-east-1.rds.amazonaws.com -P 3306 -u admin -p`

6. Run `show databases` to view databases

