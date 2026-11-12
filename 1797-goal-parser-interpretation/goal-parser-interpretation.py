class Solution(object):
    def interpret(self, command):
        ans=''
        i=0
        while i<len(command):
            if command[i] == 'G':
                ans+='G'
                i+=1
            elif command[i:i+2]=='()':
                ans+='o'
                i+=2
            else:
                ans+='al'
                i+=4
        return ans
