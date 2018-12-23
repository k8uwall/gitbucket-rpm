rm -f database.conf
yum -y install less
yum -y install java-1.8.0-openjdk
yum -y install perl
rpm -Uvh gitbucket-4.29.0-1.el7.x86_64.rpm
rpm -Uvh https://download.postgresql.org/pub/repos/yum/11/redhat/rhel-7-x86_64/pgdg-centos11-11-2.noarch.rpm
yum install -y postgresql11-server
PGSETUP_INITDB_OPTIONS="-E UTF8 --locale=C" /usr/pgsql-11/bin/postgresql-11-setup initdb
perl -pi -e 's/(peer|ident)/trust/g' /var/lib/pgsql/11/data/pg_hba.conf

systemctl start postgresql-11
sleep 3
psql -U postgres -c "CREATE ROLE gitbucket WITH LOGIN PASSWORD 'gitbucket';"
psql -U postgres -c "CREATE DATABASE gitbucket owner gitbucket;"

systemctl start gitbucket
journalctl -u gitbucket -f
