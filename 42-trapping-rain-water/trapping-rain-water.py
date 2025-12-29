class Solution:
    def trap(self,height):
        heightSize=len(height)
        if heightSize<3:
            return 0
        LM = [0] * heightSize
        RM = [0] * heightSize
        max_height = 0
        for i in range(heightSize):
            max_height = max(max_height,height[i])
            LM[i] = max_height
        max_height=0
        for i in range(heightSize -1,-1,-1):
            max_height = max(max_height, height[i]) 
            RM[i]=max_height
        water=0    
        for i in range(heightSize):
            water += min(LM[i],RM[i]) - height[i]
        return water