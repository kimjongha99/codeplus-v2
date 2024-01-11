package week2.day2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
//https://www.acmicpc.net/problem/9095

//123 더학
public class B9095 {


    static void bfs(int n) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);// 시작은 0이니깐
        int ways=0; // 방법수

        while (!queue.isEmpty()) {
            int index = queue.poll();  // 큐에서 현재 합계를 가져온다
            if(index==n){
                ways++; // 합계가 n과 일치하면 방법수 ++
            } else if (index < n) {
                queue.offer(index + 1);
                queue.offer(index + 2);
                queue.offer(index + 3);
            }
        }
        System.out.println(ways);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tc = Integer.parseInt(br.readLine());

        for (int t = 0; t < tc; t++) {
            int n = Integer.parseInt(br.readLine());
            bfs(n);
        }
    }
}
