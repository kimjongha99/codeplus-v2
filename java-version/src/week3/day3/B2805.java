package week3.day3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

//https://www.acmicpc.net/problem/2805
//나무 자르기
public class B2805 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int max=0;
        int min=0;
        int [] trees= new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            trees[i] = Integer.parseInt(st.nextToken());
            max = Math.max(trees[i], max);
        }

//        Arrays.sort(trees); // 상관없음 붙이든말던

        while (min < max) {  //이분탐색들어감
            int mid = (max+min)/2;
            long sum =0;


            for (int treeH : trees) {
                if (treeH - mid > 0) {
                    sum+= treeH-mid;
                }
            }


            if (sum < m) {
                max = mid;
            } else {
                min = mid+1;
            }


        }
        System.out.println(min - 1);



    }
}
//
//4 11
//        802
//        743
//        457
//        539
