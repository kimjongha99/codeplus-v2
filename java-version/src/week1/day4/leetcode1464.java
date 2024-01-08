package week1.day4;


//https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/


import java.util.PriorityQueue;

public class leetcode1464 {

        public int maxProduct(int[] nums) {

            PriorityQueue<Integer> queue = new PriorityQueue<>();

            for( int i : nums){
                queue.add(-i);
            }

           int n1 = queue.poll();
           int n2 = queue.poll();



            return (n1+1)*(n2+1);


        }


    public static void main(String[] args) {
        leetcode1464 sol = new leetcode1464();
        int nums [] = new int[]{3,4,5,2};
        int result = sol.maxProduct(nums);
        System.out.println(result);

    }

}
