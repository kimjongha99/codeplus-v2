package week2.day1;
//https://www.acmicpc.net/problem/2667
//단지번호 붙히기

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class B2667 {
    static int map [][];
    static boolean visited[][];
    static  int countPerDanji;

    static  int dx [] ={0,0,1,-1};
    static  int dy [] ={1,-1,0,0};

    public static void dfs(int row, int col) {
        visited[row][col] = true;
        countPerDanji++;

        for (int i = 0; i < 4; i++) {
            int newX = row + dx[i];
            int newY = col + dy[i];

            if (newX >= 0 && newX < map.length && newY >= 0 && newY < map[newX].length) {
                if (map[newX][newY] == 1 && !visited[newX][newY]) {
                    dfs(newX, newY);
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        map = new int[n][n];
        visited = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                map[i][j] = line.charAt(j) - '0';
            }
        }

        ArrayList<Integer> countList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(map[i][j]==1&&visited[i][j]==false){
                    countPerDanji=0;
                    dfs(i,j);
                    countList.add(countPerDanji);
                }
            }
        }

        System.out.println(countList.size());
        Collections.sort(countList);
        for (Integer i : countList) {
            System.out.println(i);
        }

    }
}
