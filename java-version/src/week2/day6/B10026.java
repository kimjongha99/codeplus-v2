package week2.day6;
//https://acmicpc.net/problem/10026
//적녹색약


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B10026 {
    static  char [][] graph;
    static  boolean [][] visited;
    static  int n;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};

    static void dfsR(int row, int col) {
        visited[row][col]=true;

        for (int i = 0; i < 4; i++) {
            int nx = row + dx[i];
            int ny = col + dy[i];
            if (nx >= 0 && ny >= 0 && nx < n && ny < n && visited[nx][ny] == false && graph[nx][ny] == 'R') {
                visited[nx][ny]=true;
                dfsR(nx,ny);
            }
        }

    }
    static void dfsB(int row, int col) {
        visited[row][col]=true;

        for (int i = 0; i < 4; i++) {
            int nx = row + dx[i];
            int ny = col + dy[i];
            if (nx >= 0 && ny >= 0 && nx < n && ny < n && visited[nx][ny] == false && graph[nx][ny] == 'B') {
                visited[nx][ny]=true;
                dfsB(nx,ny);
            }
        }

    }
    static void dfsG(int row, int col) {
        visited[row][col]=true;

        for (int i = 0; i < 4; i++) {
            int nx = row + dx[i];
            int ny = col + dy[i];
            if (nx >= 0 && ny >= 0 && nx < n && ny < n && visited[nx][ny] == false && graph[nx][ny] == 'G') {
                visited[nx][ny]=true;
                dfsG(nx,ny);
            }
        }

    }

    static void dfsRG(int row, int col) {
        visited[row][col]=true;
        for (int i = 0; i < 4; i++) {
            int nx = row + dx[i];
            int ny = col + dy[i];
            if (nx >= 0 && ny >= 0 && nx < n && ny < n && visited[nx][ny] == false && (graph[nx][ny] == 'R' || graph[nx][ny] == 'G')) {
                visited[nx][ny]=true;
                dfsRG(nx, ny);
            }

        }

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        graph = new char[n][n];
        visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            for (int j = 0; j < n; j++) {
                graph[i][j]=str.charAt(j);
            }
        }

        int ans=0;
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < n; col++) {
                if (graph[row][col] == 'R' &&visited[row][col]==false) {
                    dfsR(row,col);
                    ans++;
                }
                if (graph[row][col] == 'B' && visited[row][col] == false) {
                    dfsB(row, col);
                    ans++;
                }
                if (graph[row][col] == 'G' && visited[row][col] == false) {
                    dfsG(row, col);
                    ans++;
                }
            }
        }

        visited = new boolean[n][n];
        int ans2 =0;
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < n; col++) {
                if (!visited[row][col]) {
                    if (graph[row][col] == 'B') {
                        dfsB(row, col);
                    } else {
                        dfsRG(row, col);
                    }
                    ans2++;
                }
            }
        }

        System.out.println(ans+" "+ans2);
    }
}
