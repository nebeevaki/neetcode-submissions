# идем циклом и считаем количество совпадений,
# если попадается повтор, увеличиваем кол-во совпадений на один
# каждую итерацию смещаем текущий элемент на индекс числа совпадений

# цикл от 1 до len(nums)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            nums[i - count] = nums[i]
        return len(nums) - count
