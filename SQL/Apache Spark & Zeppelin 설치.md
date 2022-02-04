# Apache Spark & Zeppelin 설치

```
$ sudo apt update
$ sudo apt -y upgrade
```

- Java Install

  ```
  $ sudo apt install curl mlocate default-jdk-y
  $ java -version
  ```

- Download Apache Spark

  ```
  $ wget https://dlcdn.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
  $ tar -xvf spark-3.1.2-bin-hadoop3.2.tgz
  $ sudo mv spark-3.1.2-bin-hadoop3.2/ /opt/spark
  ```

- PATH setting

  ```
  $ vim ~/.bashrc
  ```

  ```
  export SPARK_HOME=/opt/spark
  export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
  ```

  ![Screenshot from 2022-02-04 04-17-48](/home/jngmk/Pictures/Screenshot from 2022-02-04 04-17-48.png)

  ```
  $ source ~/.bashrc
  ```

- Start master server

  ```
  $ start-master.sh
  starting org.apache.spark.deploy.master.Master, logging to /opt/spark/logs/spark-jngmk-org.apache.spark.deploy.master.Master-1-jngmk-ubuntu.out
  
  $ sudo ss -tunelp | grep 8080
  tcp    LISTEN  0       1                         *:8080                 *:*      users:(("java",pid=30634,fd=294)) uid:1000 ino:430257 sk:10 v6only:0 <->       
  ```

  - http://localhost:8080 접속

    ![image-20220204042406424](/home/jngmk/.config/Typora/typora-user-images/image-20220204042406424.png)

- Start worker process

  ```
  $ start-slave.sh spark://jngmk-ubuntu:7077
  This script is deprecated, use start-worker.sh
  starting org.apache.spark.deploy.worker.Worker, logging to /opt/spark/logs/spark-jngmk-org.apache.spark.deploy.worker.Worker-1-jngmk-ubuntu.out
  ```

  ```
  다음엔 start-worker.sh 쓰도록 하자
  ```

  - script 안뜰 시

    ```
    $ sudo updatedb
    $ locate start-worker.sh
    ```

- Spark shell(scala)

  ```
  $ /opt/spark/bin/spark-shell
  22/02/04 05:11:13 WARN Utils: Your hostname, jngmk-ubuntu resolves to a loopback address: 127.0.1.1; using 192.168.75.228 instead (on interface enp0s31f6)
  22/02/04 05:11:13 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
  WARNING: An illegal reflective access operation has occurred
  WARNING: Illegal reflective access by org.apache.spark.unsafe.Platform (file:/opt/spark/jars/spark-unsafe_2.12-3.1.2.jar) to constructor java.nio.DirectByteBuffer(long,int)
  WARNING: Please consider reporting this to the maintainers of org.apache.spark.unsafe.Platform
  WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
  WARNING: All illegal access operations will be denied in a future release
  22/02/04 05:11:14 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
  Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
  Setting default log level to "WARN".
  To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
  Spark context Web UI available at http://192.168.75.228:4040
  Spark context available as 'sc' (master = local[*], app id = local-1643919077491).
  Spark session available as 'spark'.
  Welcome to
        ____              __
       / __/__  ___ _____/ /__
      _\ \/ _ \/ _ `/ __/  '_/
     /___/ .__/\_,_/_/ /_/\_\   version 3.1.2
        /_/
           
  Using Scala version 2.12.10 (OpenJDK 64-Bit Server VM, Java 11.0.13)
  Type in expressions to have them evaluated.
  Type :help for more information.
  
  scala> 
  ```

- python

  ```
  $ /opt/spark/bin/pyspark
  Python 3.9.7 (default, Sep 16 2021, 13:09:58) 
  [GCC 7.5.0] :: Anaconda, Inc. on linux
  Type "help", "copyright", "credits" or "license" for more information.
  22/02/04 05:12:07 WARN Utils: Your hostname, jngmk-ubuntu resolves to a loopback address: 127.0.1.1; using 192.168.75.228 instead (on interface enp0s31f6)
  22/02/04 05:12:07 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
  WARNING: An illegal reflective access operation has occurred
  WARNING: Illegal reflective access by org.apache.spark.unsafe.Platform (file:/opt/spark/jars/spark-unsafe_2.12-3.1.2.jar) to constructor java.nio.DirectByteBuffer(long,int)
  WARNING: Please consider reporting this to the maintainers of org.apache.spark.unsafe.Platform
  WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
  WARNING: All illegal access operations will be denied in a future release
  22/02/04 05:12:07 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
  Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
  Setting default log level to "WARN".
  To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
  Welcome to
        ____              __
       / __/__  ___ _____/ /__
      _\ \/ _ \/ _ `/ __/  '_/
     /__ / .__/\_,_/_/ /_/\_\   version 3.1.2
        /_/
  
  Using Python version 3.9.7 (default, Sep 16 2021 13:09:58)
  Spark context Web UI available at http://192.168.75.228:4040
  Spark context available as 'sc' (master = local[*], app id = local-1643919128277).
  SparkSession available as 'spark'.
  >>> 
  ```

- Shut down

  ```
  $ $SPARK_HOME/sbin/stop-slave(worker).sh
  $ $SPARK_HOME/sbin/stop-master.sh
  ```

- zeppelin

  ```
  https://zeppelin.apache.org/download.html 접속 후 download
  ```

  ```
  $ tar -vxzf zeppelin-0.10.0-bin-all.tgz
  ```

  ```
  $ cd zeppelin-0.10.0-bin-all/conf
  $ cp zeppelin-site.xml.template zeppelin-site.xml
  $ cp zeppelin-env.sh.template zeppelin-env.sh
  ```

- PATH 문제 있을 시

  ```
  $ vim zeppelin-env.sh
  export SPARK_HOME=...
  ...
  ```

- 실행

  ```
  $ cd zeppelin-0.10.0-bin-all/
  $ bin/zeppelin-daemon.sh start
  ```

  - localhost:8080 접속 시

    ![image-20220204054124373](/home/jngmk/.config/Typora/typora-user-images/image-20220204054124373.png)

- 종료

  ```
  $ bin/zeppelin-daemon.sh stop
  ```

- Docker에서 실행

  ```
  docker run -p 8080:8080 --rm --name zeppelin apache/zeppelin:0.10.0
  ```

  