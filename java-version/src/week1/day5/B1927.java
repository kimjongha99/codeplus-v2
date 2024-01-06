package week1.day5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.Scanner;

public class B1927 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=  new BufferedReader(new InputStreamReader(System.in));
        int tc= Integer.parseInt(br.readLine());
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for (int i = 0; i < tc; i++) {
            int num= Integer.parseInt(br.readLine());

            if (num == 0) {
                if (!queue.isEmpty()) {
                    System.out.println(queue.poll());
                }else{
                    System.out.println("0");
                }

            }else{
                queue.add(num);
            }



        }
    }
}
