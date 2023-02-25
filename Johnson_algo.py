# 2 - machine scheduling
jobs = [
            # [job,machine 1 pj, machine 2 pj]
            ["A",5,2],
            ["B",1,6],
            ["C",9,7],
            ["D",3,8],
            ["E",10,4]
        ]
# [job,machine 1 pj, machine 2 pj]

# Johnson algorithm part
job_map = dict()
for job in jobs:
    job_map[job[0]] = job

job_ids = [ job[0] for job in jobs ]

def sort_func(e):
    return e[0]

# time, job id, machine
times = [(job[1],job[0],"M1") for job in jobs]
times = times + [(job[2],job[0],"M2") for job in jobs]
times.sort(key=sort_func)

answer_left = []
answer_right = []

for time in times:
    if time[1] in job_ids:
        if time[2] == "M1":
            answer_left.append(job_map[time[1]])
        else:
            answer_right.append(job_map[time[1]])
        job_ids.remove(time[1])

answer_right.reverse()
jobs = answer_left + answer_right

print(jobs)