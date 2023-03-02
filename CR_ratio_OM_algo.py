jobs = [
            ["A",2,7],
            ["B",8,16],
            ["C",4,4],
            ["D",10,17],
            ["E",5,15],
            ["F",12,18],
        ]
# (job, Pj, Dj)

def update(jobs,pj):
    for job in jobs:
        job[2] = job[2]-pj
    return jobs

answer = []
selected = [False for x in range(len(jobs))]

while(True):
    min_cr = float('inf')
    ind = -1
    swapped = False
    for j in range(len(jobs)):
        if jobs[j][2]/jobs[j][1] <= min_cr and not(selected[j]):
            ind = j
            min_cr = jobs[j][2]/jobs[j][1]
            swapped = True
    if swapped:        
        selected[ind] = True
        answer.append(jobs[ind][:2])
        jobs = update(jobs,jobs[ind][1])
    else:
        break
    
import pandas as pd
df = pd.DataFrame(answer,columns = ["Job ID","Pj"])
print(df)