# Commands for running map-reduce jobs (via docker hadoop-streming) 

## 1. Run docker:
```
docker run -it sequenceiq/hadoop-docker:2.7.1 /etc/bootstrap.sh -bash \
 ```
2. Copy files to docker:
#CONTAINER ID = dd7869fa46d6

docker cp /Users/MarinaAnanyeva/Desktop/ТМСС/bigdata/star2002-sample.csv dd7869fa46d6:/star2002-sample.csv 
docker cp /Users/MarinaAnanyeva/Desktop/ТМСС/bigdata/map1.py dd7869fa46d6:/map1.py 
docker cp /Users/MarinaAnanyeva/Desktop/ТМСС/bigdata/map2.py dd7869fa46d6:/map2.py 
docker cp /Users/MarinaAnanyeva/Desktop/ТМСС/bigdata/reduce1.py dd7869fa46d6b:/reduce1.py 
docker cp /Users/MarinaAnanyeva/Desktop/ТМСС/bigdata/Reducer2.py dd7869fa46d6:/reduce2.py

3. Create a directory in HDFS,copy files: 

hdfs dfs -mkdir task1 
bin/hdfs dfs -put /star2002-sample.csv ./task1/

4. Run Hadoop-streaming:

hadoop jar hadoop-streaming.jar \

mapper map1.py
reducer reduce1.py
input task1
output out1
[> file map1.py
file reduce1.py ]

hadoop jar hadoop-streaming.jar \

mapper map2.py
reducer reduce2.py
input task1
output out1
[> file map2.py
file reduce2.py ]
