<<<<<<< HEAD
# Smith-Waterman algorithm running on Spark paltform(python implemented)
1.You need to install some python packages(include biopython,pyspark and numpy)
=======
# SWspark
1. You need to install some python packages(include Bio,pyspark and numpy)
>>>>>>> 4ed5e3a90817a8ceffaba61b04420aa1b11c6ba8
which can be installed by Python's package manager pip.
Here are simplest way to install pacakges:

pip install biopython  

pip install numpy   

pip install pyspark  

If you can't install packages successfully,please google it.

2. now you can move all these files(include SW_align.py,SWSpark.py,query.file,
db.file,Smith_Waterman_spark.sh) to your spark direcotory.

3. move the config file to conf/ directory:
'''
 mv spark-env.sh path/to/your/spark/conf/
'''
4. Run the below command:  
'''
cd path/to/your/spark/directory  

sh Smith_Waterman_spark.sh  
'''
for my machine,it is:  

'''
cd /home/cyw/spark-2.3.1-bin-hadoop2.7/  

sh Smith_Waterman_spark.sh  
'''
5. the result will be write to files in directory aligned.csv/

6. If you want to run the single machine version Smith-waterman,please run :  

python SW_align.py  

Result will be write to 'single_machine.txt'.


