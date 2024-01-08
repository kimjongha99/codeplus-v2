package grammer;

import java.util.Stack;

public class stack {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();

        stack.add(1);
        stack.add(2);
        stack.add(3);
        System.out.println(stack);


        stack.pop();
        System.out.println(stack);


        System.out.println(stack.search(1));
    }
}
