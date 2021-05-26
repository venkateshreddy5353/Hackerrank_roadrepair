def getMinCost(crew_id, job_id):
    print(crew_id,job_id)
    crew_id.sort()
    job_id.sort()
    l1=len(crew_id)
    l2=len(job_id)
    cost_list=[]
    if l1==l2:
        for i in range(l1):
            if job_id[i]>=crew_id[i]:
                print("Entered if")
                cost_list.append(job_id[i]-crew_id[i])
                
            elif job_id[i]<crew_id[i]:
                print("Entered elif")
                cost_list.append(crew_id[i]-job_id[i])
               
            s=sum(cost_list)
    return s
  
