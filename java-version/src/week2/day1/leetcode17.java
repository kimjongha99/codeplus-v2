package week2.day1;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class leetcode17 {
    private static final String[] KEYPAD = {
            "",    // 0
            "",    // 1
            "abc", // 2
            "def", // 3
            "ghi", // 4
            "jkl", // 5
            "mno", // 6
            "pqrs", // 7
            "tuv", // 8
            "wxyz" // 9
    };

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();

        Stack<String> stack = new Stack<>();
        stack.push("");

        while (!stack.isEmpty()) {
            String combination = stack.pop();
            if (combination.length() == digits.length()) {
                result.add(combination);
            } else {
                String nextDigits = KEYPAD[digits.charAt(combination.length()) - '0'];
                for (char c : nextDigits.toCharArray()) {
                    stack.push(combination + c);
                }
            }
        }

        return result;
    }



    public static void main(String[] args) {
        leetcode17 solution = new leetcode17();
        List<String> combinations = solution.letterCombinations("23");
        System.out.println(combinations);
    }
}
