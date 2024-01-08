package week1.day5;

import java.io.*;
import java.util.Stack;

public class B5397 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int tc = Integer.parseInt(br.readLine());

        for (int t = 0; t < tc; t++) {
            Stack<Character> leftStack = new Stack<>();
            Stack<Character> rightStack = new Stack<>();
            String str =  br.readLine();



            for (char c : str.toCharArray()) {
                switch (c){
                    case '<':
                        if(!leftStack.isEmpty()){
                            rightStack.push(leftStack.pop());
                        }
                        break;
                    case '>':
                        if(!rightStack.isEmpty()){
                            leftStack.push(rightStack.pop());
                        }
                        break;
                    case '-':
                        if (!leftStack.isEmpty()) {
                            leftStack.pop();
                        }
                        break;
                    default:
                        leftStack.push(c);
                        break;
                }
            }


            //이제 스택 출력 근데 뒤집어야댐
            Stack <Character> reverseStack = new Stack<>();

            while (!leftStack.isEmpty()) {
                reverseStack.push(leftStack.pop());
            }

            while (!reverseStack.isEmpty()) {
                bw.write(reverseStack.pop());
            }
            while (!rightStack.isEmpty()) {
                bw.write(rightStack.pop());
            }
            bw.newLine();





        }
        br.close();
        bw.flush();

    }
}
