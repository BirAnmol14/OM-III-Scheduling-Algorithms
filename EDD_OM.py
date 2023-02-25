jobs = [
            ["A",7,8],
            ["B",1,12],
            ["C",5,6],
            ["D",2,4],
            ["E",6,18]
        ]
# (job, Pj, Dj)

def sort_func(e):
    return e[2]

def print_jobs(jobs,total_f,max_f,total_l,max_l,total_t,max_t,n_t,total_w,max_w):
    print()
    print("EDD")
    print("********")
    print("(job, Pj, Dj,Fj,Lj,Tj,Is Tardy?, Wait Time)")
    for job in jobs:
        print(job)
        print()
    print("********")
    print("(Total flow, Max Flow [MAKE-SPAN], Total Lateness, Max Lateness, Total Tardiness, Max Tardiness, No of Tardy jobs, Total Wait, Max Wait)")
    print([total_f,max_f,total_l,max_l,total_t,max_t,n_t,total_w,max_w])
    print()
     
jobs.sort(key=sort_func)

# (job, Pj, Dj,Fj,Lj,Tj,Is Tardy?, Wait Time)
# max Fj = Make span
# Total Fj
# max Lj, total Lj
# Max tardiness
# No of tardy jobs

max_f = float('-inf')
max_l = float('-inf')
max_t = float('-inf')
max_w = float('-inf')
n_t = 0
total_f = 0
total_l = 0
total_t = 0
total_w = 0
prev_f = 0

for job in jobs:
    f = job[1]+prev_f
    prev_f = f
    total_f = total_f + f
    if(max_f<f):
        max_f = f 
        
    l = f - job[2]
    if(max_l<l):
        max_l = l
    total_l = total_l+l
    
    t = max(0,l)
    if(max_t<t):
        max_t = t
    total_t = total_t + t
    if t > 0:
        n_t = n_t+1
    w = f-job[1]
    if(max_w<w):
        max_w = w
    total_w = total_w + w
    job.extend([f,l,t,t>0,w])
    
print_jobs(jobs,total_f,max_f,total_l,max_l,total_t,max_t,n_t,total_w,max_w)