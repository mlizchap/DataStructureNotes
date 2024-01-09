# recursive
def permutations(nums):
    def helper(i):
      if i == len(nums):
          return [[]]
      
      resPerms = []
      perms = helper(i + 1)
      for p in perms:
          for j in range(len(p) + 1):
              pCopy = p.copy()
              pCopy.insert(j, nums[i])
              resPerms.append(pCopy)
      return resPerms

    return helper(0)
        
ans = permutations([1, 2, 3])
print(ans)
