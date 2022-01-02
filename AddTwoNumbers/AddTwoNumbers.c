/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* result = (struct ListNode*)malloc(sizeof(*result));
    result->val = 0;
    result->next = NULL;
    struct ListNode* temp = result;
    int carry = 0;
    struct ListNode* p = l1;
    struct ListNode* q = l2;
    while (p != NULL || q != NULL) {
        int p_digit = (p != NULL) ? p->val : 0;
        int q_digit = (q != NULL) ? q->val : 0;
        int sum = carry + p_digit + q_digit;
        carry = sum / 10;
        struct ListNode* cell = (struct ListNode*)malloc(sizeof(*cell));
        cell->val = sum % 10;
        cell->next = NULL;
        temp->next = cell;
        temp = temp->next;
        if (p != NULL) {
            p = p->next;
        }
        if (q != NULL) {
            q = q->next;
        }
    }
    if (carry > 0) {
        struct ListNode* cell = (struct ListNode*)malloc(sizeof(*cell));
        cell->val = carry;
        cell->next = NULL;
        temp->next = cell;
    }
    return result->next;
}