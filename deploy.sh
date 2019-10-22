rm -rf ffninja
wget https://github.com/maxhumber/ffninja/archive/master.zip
unzip master.zip
mv ffninja-master ffninja
rm -f master.zip
cd ffninja
make stop
make cleanup
make build
make run
