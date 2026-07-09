class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        count=0
        i=0
        j=0
        n=len(players)
        m=len(trainers)
        while i<n and j <m:
            if players[i] <= trainers[j]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count


