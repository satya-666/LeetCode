class Solution(object):
    def numRescueBoats(self, people, limit):
        cout = 0
        people.sort()
        i,j = 0,len(people)-1
        while i<=j:
            if people[i]+people[j]<= limit:
                cout+=1
                j-=1
                i+=1
            elif people[i]+people[j]> limit:
                cout+=1
                j-=1
        return(cout)
        