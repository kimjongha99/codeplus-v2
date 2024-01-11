package week2.day1;

//https://www.acmicpc.net/problem/2606
//바이러스


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class B2606 {
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static int count;
    static int n;

    static void dfs(int start) {
        visited[start] = true;
        count++;

        for (int i : graph[start]) {
            if (!visited[i]) {
                dfs(i);
            }
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int com = Integer.parseInt(br.readLine());
         n = Integer.parseInt(br.readLine());

        graph= new ArrayList[com+1];
        for (int i = 1; i <= com; i++) {
            graph[i] = new ArrayList<>();
        }
        visited = new boolean[com+1];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        dfs(1);
        System.out.println(count - 1);




    }
}
