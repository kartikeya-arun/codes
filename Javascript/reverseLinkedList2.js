/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function (head, left, right) {
  const dummy = new ListNode(0, head);
  let cur = head;
  let prev = null;
  let prevLeft = dummy;
  // Phase 1
  for (i = 0; i < left - 1; i++) {
    prevLeft = cur;
    cur = cur.next;
  }
  // Phase 2
  for (i = 0; i < right - left + 1; i++) {
    let nxt = cur.next;
    cur.next = prev;
    prev = cur;
    cur = nxt;
  }
  // Phase 3
  prevLeft.next.next = cur;
  prevLeft.next = prev;
  return dummy.next;
};
