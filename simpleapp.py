from pyspark import SparkContext
from Bio.SubsMat import MatrixInfo
import time
import SW_align
start_time = time.time()
sc =SparkContext()
# substitute matrix blosum50
sub_mat = MatrixInfo.blosum50
#sub_mat = sc.broadcast(sub_mat)
# read files and 
db = sc.textFile('db.file')
db =db.map(lambda x: x.split(','))
#print(db.take(20))
query = sc.textFile('query.file')
query = query.collect()[0]
#query = sc.broadcast(query)
aligned = db.map(lambda x:SW_align.alignment(dbs=x,query=query,sub_mat=sub_mat))
#element in this rdd looks like:(seq_name,max_score,aligned_db,aligned_query)
ks = [3,5,7]
for k in ks:
    top_k = aligned.sortBy(lambda x:x[1],ascending=False).take(k)
    file_name = 'top_'+str(k)+'_result'
    f = open(file_name,'w')
    f.write('#seq_name, #max_score, #aligned_db ,#aligned_query\n')
    for ele in top_k:
        f.write(str(ele))
        f.write('\n')
    print(top_k)
used_time = time.time()-start_time

print('program running time:%.4f'%used_time)
'''
def del_change_line(s):
    s[1]=s[1][0:-1]
    return[s[0],s[1]]
db = db.map(del_change_line)
print(db.collect())
'''
