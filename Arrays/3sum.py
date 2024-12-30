
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n - 2):
            if i > 0 and (nums[i] == nums[i-1]):
                continue
            req = 0 - nums[i] # 0 is target value
            low = i + 1
            high = n - 1

            while low < high:

                sum = nums[low] + nums[high]
            
                if sum == req:
                    op = [nums[i],nums[low] , nums[high]]
                    res.append(op)
                    low += 1
                    high -= 1

                    while low < high and nums[low] == nums[low - 1]:
                        low += 1

                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1

                elif sum < req:
                    low += 1
                    
                else:
                    high -= 1

        return res

            
print(Solution().threeSum(nums = [41204,6323,5021,27767,-18684,89279,16935,-10093,-9753,-5202,83041,9491,35206,-3786,25148,-989,1290,68246,-13583,-3574,-8125,-2680,80013,47302,-8711,45233,5497,13996,-8707,61757,27122,-544,-3638,-12466,80860,86309,-4842,74323,74240,29760,98678,23623,98540,-7551,-18859,88487,82031,-17613,71005,73696,-8448,53294,-10696,-929,62455,74509,93579,-11159,11536,34075,29519,-6394,29421,-18852,-4961,-2334,-8317,59554,-1801,64592,20842,-19027,-524,-6596,-1414,-9478,6543,27221,-11680,-16476,88651,27805,-16367,17146,11928,36835,-99,-6949,44255,52382,28303,99208,46608,-3067,13065,-5331,-4633,48678,-9613,-18268,-4377,-17956,14915,56875,22797,-18734,-10635,-3348,-9211,97693,-10507,23534,-14942,77612,58511,-9194,-19819,-13038,94266,96461,-3897,-6247,-785,-12829,5269,17991,-12346,-9287,51982,98503,-3490,12742,24162,-1390,-6575,-670,83307,61945,-12620,-12110,-15201,-10278,-5947,34532,55069,48334,22250,-4370,29072,-16625,-18186,60743,36203,35731,15655,-9106,-5734,-8486,-18688,-10956,55323,-17637,-16699,40430,31738,-2606,67304,86606,-11082,84814,97802,-4539,-5724,-10162,-11103,-5814,-3475,-15929,-12242,-3171,-632,96688,43135,-1371,16611,33,-6713,-13057,-8712,-12406,82814,65391,-13261,26526,-12659,39875,-17915,-14485,-10922,-16085,95980,45573,-16364,-302,8883,-7677,-8509,86579,-17516,5895,36203,42776,-8548,91988,-19282,-3541,-14395,-2986,29311,14573,89469,80989,-869,86805,-12341,15157,-10109,69639,71687,-9862,1965,-13909,83567,-13164,54106,-9985,41727,2149,7209,37164,20572,-19903,59087,99083,40075,80674,10693,-1080,48281,-1108,40199,57201]))