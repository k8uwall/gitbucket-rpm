# gitbucket
gitbucket rpm

## how to build

```
curl -LO https://github.com/gitbucket/gitbucket/releases/download/4.29.0/gitbucket.war
mkdir -p build/rpm/SOURCES/
mv gitbucket.war build/rpm/SOURCES/
make
```

## how to install (example)

```
mkdir -m 777 data
mkdir -m 777 db
cp build/rpm/RPMS/x86_64/gitbucket-4.29.0-1.el7.x86_64.rpm data/
sh docker_centos.sh
cd /gitbucket
sh build.sh
```
