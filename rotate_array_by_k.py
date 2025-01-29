# first solution  
def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l, r = 0, len(nums)-1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l , r = l+1, r-1 


        l, r = k, len(nums)-1 
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l , r = l+1, r-1

        l, r = 0, k-1 
        while l < r:
            nums[l], nums[r] = nums[r], nums[l] 
            l , r = l+1, r-1       
     
        return nums 

# 2nd solution

  def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        rotated = [0] * n

        for i in range(n):
            rotated[(i + k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = rotated[i]
