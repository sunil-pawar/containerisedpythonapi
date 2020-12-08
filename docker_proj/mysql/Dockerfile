#renamed dockerfile to Dockerfile
# Derived from official mysql image (our base image)

FROM mysql:5.7
# Add a database and root password
ENV MYSQL_DATABASE=clients MYSQL_ROOT_PASSWORD=root MYSQL_ROOT_HOST=%

# Add the content of the sql-scripts/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup

COPY initialise_db_tb.sql /docker-entrypoint-initdb.d/
# Setup the custom configuration
COPY mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf
#COPY my.cnf /etc/mysql/conf.d/my.cnf
#COPY my.cnf /etc/
#COPY my.cnf /etc/mysql/
