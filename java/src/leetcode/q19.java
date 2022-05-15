package leetcode;

public class q19 {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int length = 0;
        ListNode tmp = head;
        while (tmp != null) {
            tmp = tmp.next;
            length += 1;
        }

        ListNode root= new ListNode();
        root.next = head;

        ListNode now = root;
        ListNode prev = root;
        for (int i=0; i<=length-n; i++) {
            prev = now;
            now = now.next;
        }

        prev.next = now.next;

        return root.next;
    }

    public static void main(String[] args){
        ListNode node = new ListNode(1);
        q19 q = new q19();
        System.out.println(q.removeNthFromEnd(node, 1));
    }
}


class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
