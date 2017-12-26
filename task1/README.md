### Docker hadoop-streming 
### Run commands for Map-Reduce jobs

## Task 1: Hadoop Streaming
```
1. Для каждого значения antiNucleus вычислить среднее значение prodTime
2. Взять строки, у которых prodTime выше среднего для соответствующего ему antiNucleus
3. Для каждого antiNucleus посчитать:
    1. Количество уникальных значений eventFile
    2. Среднее значение Pt 
```
    
<b>Variables:</b>
<pre>
0. antiNucleus INT
1. eventFile UINT
2. eventNumber INT
3. eventTime DOUBLE
4. histFile UINT
5. multiplicity INT
6. NaboveLb INT
7. NbelowLb INT
8. NLb  INT
9. primaryTracks INT
10. prodTime DOUBLE
11. Pt  FLOAT
12. runNumber INT
13. vertexX  FLOAT
14. vertexY  FLOAT
15. vertexZ  FLOAT
</pre>

## 1. Run docker:
```
docker run -it sequenceiq/hadoop-docker:2.7.1 /etc/bootstrap.sh -bash
 ```
## 2. Copy files to docker:
(CONTAINER ID = dd7869fa46d6)
```
docker cp /Users/MarinaAnanyeva/Desktop/ТМСС/bigdata/star2002-sample.csv dd7869fa46d6:/star2002-sample.csv  
docker cp /Users/MarinaAnanyeva/Desktop/ТМСС/bigdata/map1.py dd7869fa46d6:/map1.py 
docker cp /Users/MarinaAnanyeva/Desktop/ТМСС/bigdata/map2.py dd7869fa46d6:/map2.py
docker cp /Users/MarinaAnanyeva/Desktop/ТМСС/bigdata/reduce1.py dd7869fa46d6b:/reduce1.py
docker cp /Users/MarinaAnanyeva/Desktop/ТМСС/bigdata/Reducer2.py dd7869fa46d6:/reduce2.py
 ```
## 3. Create a directory in HDFS,copy files: 
```
cd $HADOOP_PREFIX
bin/hdfs dfs -mkdir task1
bin/hdfs dfs -put /star2002-sample.csv ./task1/
 ```
 
## 4. Run Hadoop-streaming:
 ```
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
    -input task1/ \
    -output ./output \
    -mapper map1.py \
    -reducer reduce1.py \
    -file /map1.py \
    -file /reduce1.py
 
 bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
    -input task1/ \
    -output ./output \
    -mapper map2.py \
    -reducer reduce2.py \
    -file /map2.py \
    -file /reduce2.py
 ```
