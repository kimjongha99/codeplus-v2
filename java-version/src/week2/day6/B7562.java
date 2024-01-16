package week2.day6;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

//https://www.acmicpc.net/problem/7562
//나이트의 이동
public class B7562 {
    static  boolean[][] visited;
    static int dx[] = {-2,-2,-1,1,2,2,-1,1};
    static int dy[] = {1,-1,2,2,-1,1,-2,2};

    static  int n;
    static int bfs(int x,int  y,int  x1, int y1) {
        Queue<int []> queue = new LinkedList<>();
        queue.add(new int[]{x, y, 0});  // The third value in the array is the count of moves
        visited[x][y] = true;

        while (!queue.isEmpty()) {
            int now[] = queue.poll();
            visited[now[0]][now[1]]=true;

            if (now[0] == x1 && now[1] == y1) {
                return now[2];  // Return the count when the target is reached
            }

            for (int i = 0; i < 8; i++) {
                int nx = now[0]+dx[i];
                int ny = now[1]+dy[i];

                if (nx >= 0 && ny >= 0 && nx < n && ny < n && !visited[nx][ny]) {
                    visited[nx][ny]=true;
                    queue.add(new int[]{nx, ny, now[2] + 1});
                }
            }
        }
        return 0;  // 해당 테스트 케이스의 이동 횟수를 반환

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        for (int t=0; t < tc; t++) {
            n = Integer.parseInt(br.readLine());
            visited = new boolean[n][n];


            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());


            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());

            int count = bfs(x, y, x1, y1);  // 해당 테스트 케이스의 이동 횟수를 얻음
            System.out.println(count);

        }
    }
}
//      for (int i = 0; i < graph.length; i++) {
//        System.out.println();
//        for (int j = 0; j < graph[0].length; j++) {
//        System.out.print(graph[i][j]);
//        }
//        }
