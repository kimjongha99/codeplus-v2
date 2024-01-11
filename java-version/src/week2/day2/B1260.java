package week2.day2;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

//https://www.acmicpc.net/problem/1260
//DFS 와 BFS
public class B1260 {
    static int [][] graph;
    static boolean [] visited;

    static int n,m,k;
    static void dfs(int start) {
        visited[start] = true;
        System.out.print(start + " ");
        for (int i = 1; i <= n; i++) {
            if (graph[start][i] == 1 && visited[i] == false) {
                dfs(i);
            }
        }
    }

    static void bfs(int start) {
        visited = new boolean[n + 10];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start]=true;

        while (!queue.isEmpty()) {
            int idx = queue.poll();
            System.out.print(idx+" ");
            for (int i = 1; i <= n; i++) {
                if (visited[i] == false && graph[idx][i] == 1) {
                    queue.add(i);
                    visited[i] = true;

                }


            }
        }


    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
         n = Integer.parseInt(st.nextToken());
         m = Integer.parseInt(st.nextToken());
         k = Integer.parseInt(st.nextToken());

        graph =new int[n+10][n+10];
        visited = new boolean[n+10];

        for (int i = 0; i < m; i++) {
                st =new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                graph[x][y]=graph[y][x]=1;
        }

        dfs(k);
        System.out.println();
        bfs(k);



    }
}
