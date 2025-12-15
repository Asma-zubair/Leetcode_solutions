from typing import List
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mention=[0]*numberOfUsers
        online=[True]*numberOfUsers
        online_until=[0]*numberOfUsers

        #convert time in strings
        for event in events:
             event[1]=int(event[1])

        #sort on bases of time
        events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))


        for event in events:
            typ=event[0] #EVENT
            t=event[1]  #time

            #for coming online again
            for i in range(numberOfUsers):
                if not online[i] and t >= online_until[i]:
                    online[i]=True
            
            if typ=="OFFLINE":
                user=int(event[2]) #ids
                online[user]=False
                online_until[user]=t+60

            else:
                msg=event[2]

                if msg=="ALL":
                    for i in range(numberOfUsers):
                        mention[i]+=1
                    continue

                if msg == "HERE":
                 for i in range(numberOfUsers):
                    if online[i]:
                         mention[i] += 1
                 continue   

       
                tokens = msg.split()
                for tok in tokens:
                    if tok.startswith("id"):
                        uid = int(tok[2:])
                        mention[uid] += 1
        return mention


                                

            
            