#SWspark
1. You need to install some python packages(include Bio,pyspark and numpy)
which can be installed by Python's package manager pip.
Here are simplest way to install pacakges:

pip install biopython  

pip install numpy   

pip install pyspark  

If you can't install packages successfully,please google it.

2. now you can move all these files(include SW_align.py,simpleapp.py,query.file,
db.file,Smith_Waterman_spark.sh) to your spark direcotory.

3. run the below command:  
sh path/to/your/spark/directory/Smith_Waterman_spark.sh  
for my machine,it is:  
sh /home/cyw/spark-2.3.1-bin-hadoop2.7/Smith_Waterman_spark.sh

4. the result will be write in the 'top_k_result' file,where k=(3,5,7)


