docker stop centos7
docker rm centos7
docker run --privileged -d -v `pwd`/data:/gitbucket -v `pwd`/db:/var/lib/pgsql/11/ -p 8080:8080 --name centos7 centos:centos7 /sbin/init
docker exec -it centos7 /bin/bash
