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
    static int [][] graph;  //2차원 배열의 그래프를 만들어준다.
    static boolean [] visited;  // 방문배열

    static int n,m,k;
    static void dfs(int start) {
        visited[start] = true;  // 바로 방문배열에 시작인덱스번호를 true로 바꾸고 재방문 하지않게 한다.
        System.out.print(start + " "); // 여기서 방문한 노드를 출력한다.
        for (int i = 1; i <= n; i++) {  //노드의 1번 부터 n번까지 순회
            if (graph[start][i] == 1 && visited[i] == false) { // 그래프가 1, 즉 존재하고  방문을 안했으면 dfs
                dfs(i);
            }
        }
    }

    static void bfs(int start) {
        visited = new boolean[n + 10]; //방문배열이 dfs로 인해 다 방문처리되어서 다시 초기화
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start); //큐에 시작노드 추가
        visited[start]=true;  //시작 노드를 방문처리.

        while (!queue.isEmpty()) {  // 큐가 비어있을때까지 반복
            int idx = queue.poll();  // idx에 현재노드 뽑아냄.
            System.out.print(idx+" "); // 현재노드 출력
            for (int i = 1; i <= n; i++) {  // 여기서 방문한 노드를 출력한다.
                if (visited[i] == false && graph[idx][i] == 1) {     // 그래프가 1, 즉 존재하고  방문을 안했으면 dfs
                    queue.add(i);  // 노드를 추가하고
                    visited[i] = true; // 방문처리.
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

        graph =new int[n+10][n+10];  //그래프를 초기화 해준다.  +10을 한이유는 배열을 좀더 넉넉히 잡기위해서 n 으로해도 무방
        visited = new boolean[n+10]; // 마찬가지

        for (int i = 0; i < m; i++) {
                st =new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                graph[x][y]=graph[y][x]=1;  //2차원 그래프 상의   입력받은 위치를 1로 표시한다.
        }

        dfs(k); // dfs 들어감
        System.out.println();
        bfs(k); // bfs



    }
}
