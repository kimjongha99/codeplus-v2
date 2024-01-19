package week3.day3;
//https://www.acmicpc.net/problem/1654
//랜선 자르기

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1654 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st =new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int[] lan = new int[k];
        int max=0;
        int min=0;

        for (int i = 0; i < k; i++) {
            lan[i] = Integer.parseInt(br.readLine());
            max = Math.max(lan[i], max);
        }


        while (min < max) {
            int mid = (max + min)/2;
            long count = 0;



            for (int lan_len : lan) {
                count+= lan_len/mid;
            }



            if(count < n) {
                max = mid;
            }
            else {
                min = mid + 1;
            }


        }

        System.out.println(min - 1);

    }
}
