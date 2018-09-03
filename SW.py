import numpy as np
class SW(object):
    def __init__(self, seq1, seq2, sub_mat):
        self.seq1 = seq1
        self.seq2 = seq2 
        self.sub_mat = sub_mat
    def alignment(self, gap_o=5, gap_e=1):
        # return the score matrix
        m = len(seq1)
        n = len(seq2)
        score_matrix = np.zeros(shape=(m+1,n+1))
        # fill in the M_{i,j} M is the score matrix
        for i in range(1,m+1):
            for j in range(1,n+1):
                temp_score = [0]
                I_list = [score_matrix[i][j-ele]-(gap_o+(ele-1)*gap_e) for ele in range(1,j)]
                J_list = [score_matrix[i-ele][j]-(gap_o+(ele-1)*gap_e) for ele in range(1,i)]
                if len(I_list)>0:
                    temp_score.append(max(I_list))
                if len(J_list)>0:
                    temp_score.append(max(J_list))
                if (seq1[i-1],seq2[j-1]) in sub_mat:
                    temp_score.append(score_matrix[i-1,j-1]+self.sub_mat[(seq1[i-1],seq2[j-1])])
                else:
                    temp_score.append(score_matrix[i-1,j-1]+self.sub_mat[(seq2[j-1],seq1[i-1])])
                score_matrix[i,j] = max(temp_score)
        self.score_matrix = score_matrix
    def obtain_best_local_alignment(self):
        #max_index = np.unravel_index(np.argmax(self.score_matrix,axis=None),self.score_matrix.shape)
        # Trace_back
        max_dict = {}
        max_temp = 0
        score_matrix = self.score_matrix
        for i in range(score_matrix.shape[0]):
            for j in range(score_matrix.shape[1]):
                if self.score_matrix[(i,j)]<max_temp:
                    pass
                else:
                    max_temp = score_matrix[(i,j)]
                    max_dict[(i,j)] = max_temp
        M = max(max_dict.values())
        max_dict_update = {}# {(1,2):4} i.e.{coordinates:value}
        for ele in max_dict:
            if max_dict[ele] == M:
                max_dict_update[ele]=M
        def traceback(index,traceback_list):
            indexes = dict(
            left = (index[0]-1,index[1]),
            up  = (index[0],index[1]-1),
            left_up  = (index[0]-1,index[1]-1)
            )
            values = {}
            for ele in indexes:
                values[ele]=(score_matrix[indexes[ele]])
            max_key = max(values,key=values.get)
            #max_value = max(values.values())
            if min(values.values()) > 0:
                traceback_list.append(indexes[max_key])
                traceback(indexes[max_key],traceback_list)
        traceback_result = {}  # {source_index:[indexes]}
        for ele in max_dict_update:
            traceback_result[ele] = [ele]
            traceback(ele,traceback_result[ele])
            traceback_result[ele] = list(reversed(traceback_result[ele]))
        # obtain aligned sequences
        seq1_index = []
        seq2_index = []
        #print(traceback_result)
        for ele in traceback_result:
            for elem in traceback_result[ele]:
                if elem[0]>0:
                    seq1_index.append(elem[0]-1)
                else:
                    seq1_index.append(elem[0])
                if elem[1]>0:
                    seq2_index.append(elem[1]-1)
                else:
                    seq2_index.append(elem[1])

        #print(seq1_index)
        #print(seq2_index)
        aligned_seq1 = ''
        last_num = ''
        for num in seq1_index:
            if num == last_num:
                aligned_seq1+='-'
            else:
                aligned_seq1+=self.seq1[num]
            last_num = num
        aligned_seq2 = ''
        last_num = ''
        for num in seq2_index:
            if num == last_num:
                aligned_seq2+='-'
            else:
                aligned_seq2+=self.seq2[num]
            last_num = num
        return aligned_seq1,aligned_seq2




        
        

            



        
if __name__ == "__main__":
    # test the program
    seq1 = 'GGTTGACTA'
    seq2 = 'TGTTACGG'
    print('primary sequences:')
    print((seq1,seq2))
    bases = ["A","T","C","G"]
    sub_mat = {}
    for i in range(len(bases)):
        for j in range(i,len(bases)):
            if i==j:
                sub_mat[(bases[i],bases[j])] =3
            else:
                sub_mat[(bases[i],bases[j])] =-3
    #print(sub_mat)
    sw = SW(seq1,seq2,sub_mat)
    M = sw.alignment(gap_e=1,gap_o=1)
    #print(M)
    aliged_seqs = sw.obtain_best_local_alignment()
    print("after Sw:")
    print(aliged_seqs)



    
