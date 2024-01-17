package week3;
//                https://leetcode.com/problems/largest-number/
//                        179. Largest Number


import week1.day4.leetcode1337;

import java.util.Arrays;
import java.util.Comparator;

public class leetcode179 {
     static String largestNumber(int[] nums) {
        String[] asStrs = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            asStrs[i] = String.valueOf(nums[i]);
        }

         Arrays.sort(asStrs, new Comparator<String>() {
             @Override
             public int compare(String a, String b) {
                 String order1 = a + b;
                 String order2 = b + a;
                 return order2.compareTo(order1);
             }
         });
         if (asStrs[0].equals("0")) {
             return "0";
         }
         StringBuilder largestNumberStr = new StringBuilder();
        for (String str : asStrs) {
        largestNumberStr.append(str);
    }

        return largestNumberStr.toString();


}


    public static void main(String[] args) {
        int[] nums = {3, 30, 34, 5, 9};
        System.out.println(largestNumber(nums));
    }
    }

