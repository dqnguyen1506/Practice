class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode x = new ListNode(0);
        ListNode y = l1, z = l2, curr = x; 
        int carry = 0, num1 , num2, sum;
        while(y != null || z != null){
            if(y != null){
                num1 = y.val;
            }else{num1 = 0;}

            if(z != null){
                num2 = z.val;
            }else{num2 = 0;}
            sum = num1 + num2 + carry;
            carry = sum / 10;
            curr.next = new ListNode(sum % 10); //move sum to the next spot on the linked list (0-9)
            curr = curr.next;
            if(y != null){
                y = y.next;
            }
            if(z != null){
                z = z.next;
            }
        }

        if(carry > 0){
            curr.next = new ListNode(carry);
        }
        return x.next;
    }
}