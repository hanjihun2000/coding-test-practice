/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

struct element {
    int value;
    int index;
} element;

typedef struct element* elementT;

int* maxSubsequence(int* nums, int numsSize, int k, int* returnSize) {
    *returnSize = k;
    elementT elementArr = (elementT)malloc(sizeof(elementArr) * numsSize);
    for (int i = 0; i < numsSize; i++) {
        elementArr[i].value = nums[i];
        elementArr[i].index = i;
    }

    for (int i = 1; i < numsSize; i++) {
        for (int j = i; j > 0 && elementArr[j].value > elementArr[j - 1].value; j--) {
            {
                int tempValue = elementArr[j].value;
                int tempIndex = elementArr[j].index;
                elementArr[j].value = elementArr[j - 1].value;
                elementArr[j].index = elementArr[j - 1].index;
                elementArr[j - 1].value = tempValue;
                elementArr[j - 1].index = tempIndex;
            }
        }
    }

    for (int i = 0; i < numsSize; i++) {
        printf("%d\n", elementArr[i].index);
    }

    for (int i = 0; i < (*returnSize); i++) {
        for (int j = i; j > 0 && elementArr[j].index < elementArr[j - 1].index; j--) {
            {
                int tempValue = elementArr[j].value;
                int tempIndex = elementArr[j].index;
                elementArr[j].value = elementArr[j - 1].value;
                elementArr[j].index = elementArr[j - 1].index;
                elementArr[j - 1].value = tempValue;
                elementArr[j - 1].index = tempIndex;
            }
        }
    }

    int* returnArr = (int*)malloc(sizeof(int) * (*returnSize));
    for (int i = 0; i < (*returnSize); i++) {
        returnArr[i] = elementArr[i].value;
    }
    return returnArr;
}