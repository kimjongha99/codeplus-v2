
package week1.day5;
public class leetcode206 {

    class ListNode {
        int val;
        ListNode next;
    }


    public ListNode reverseList(ListNode head) {
        if(head == null ){
            return head;
        }

        ListNode prev = null;
        ListNode curr = head;

        while (curr != null){

            ListNode next_temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next_temp;
        }
        return prev;
    }

}
