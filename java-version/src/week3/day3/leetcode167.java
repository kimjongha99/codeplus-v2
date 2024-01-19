package week3.day3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

//https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
//167. Two Sum II - Input Array Is Sorted
public class leetcode167 {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;

        while (left < right) {
            int currentSum = numbers[left] + numbers[right];
            if (currentSum == target) {
                return new int[]{left + 1, right + 1};
            } else if (currentSum < target) {
                left++;
            } else {
                right--;
            }
        }

        return new int[]{-1, -1};
    }
    public static void main(String[] args) {
        leetcode167 sol = new leetcode167();

        // Test cases
        System.out.println(sol.twoSum(new int[]{2, 7, 11, 15}, 9)); // Expected output: [1, 2]


    }
}
