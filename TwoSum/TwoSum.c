/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        for (int j = i + 1; j < numsSize; j++) {
            int y = target - x;
            if (nums[j] == y) {
                int* result = (int*)malloc(sizeof(*result) * 2);
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                return result;
            }
        }
    }
    return NULL;
}