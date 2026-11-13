class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2

            arr = matrix[mid]

            arr_low = 0
            arr_high = len(arr) - 1

            while arr_low <= arr_high:
                arr_mid = (arr_low + arr_high) // 2

                if arr[arr_mid] == target:
                    return True
                
                if arr[arr_mid] > target:
                    arr_high = arr_mid - 1
                elif arr[arr_mid] < target:
                    arr_low = arr_mid + 1
            
            if arr[arr_mid] > target:
                high = mid - 1
            elif arr[arr_mid] < target:
                low = mid + 1
        
        return False