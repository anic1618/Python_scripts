'''
convert darknet yolov3 output tocsv file
'''

'''
Enter Image Path: /workspace/......../1.jpg: Predicted in 12.937000 milli-seconds.
B: 58%	(left_x:  329   top_y:  287   width:   77   height:  154)
T: 84%	(left_x:  483   top_y: 1063   width:  248   height:  130)
Enter Image Path: /workspace/......../10.jpg: Predicted in 12.690000 milli-seconds.
T: 75%	(left_x:  480   top_y: 1071   width:  116   height:   56)
D: 60%	(left_x:  606   top_y:  351   width:  142   height:  981)
B: 81%	(left_x:  845   top_y:  536   width:   96   height:  109)
020819
'''
import sys
#UPLOAD_FOLDER = 'upload'

result_file_path = sys.argv[1]#'result.txt'
print(result_file_path);
#exit()
final_txt = sys.argv[1]+'.csv'
with open(result_file_path,"r") as f:
    data = f.readlines()
    
ffinal = open(final_txt,"w")

name = {'B':Boy, 'T':Toy}
i = 0
while i < len(data):
    resultstr=''
    parts = data[i].split(':')   
    print(parts)
    if (parts[0] == 'Enter Image Path'):
        filepath = parts[1].split('/') 
        filename = filepath[-1] 
        resultstr = filename + ','
        i+=1
        cnt = {'T':0,'B':0,'G':0,'W':0,'D':0,'P':0,'N':0}
        while i < len(data) and data[i].split(':')[0] != 'Enter Image Path':
            cnt[data[i][0]] = 1
            i+=1

        """
        for k in cnt:
            if cnt[k] == 1:
                resultstr =resultstr+ name[k] + ","
        resultstr += "\n"
        """
        for k in ('B','T','G'):
           if cnt[k] == 1:
                resultstr =resultstr+ k
           resultstr += ","
        resultstr += "\n"
           
    ffinal.write(resultstr)
    #if next line has no detect
    

ffinal.close()
