package week3.day1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
//https://www.acmicpc.net/problem/5052
//전화번호 목록

public class B5052 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        for (int t = 0; t < tc; t++) {
            int n = Integer.parseInt(br.readLine());
            String[] lst = new String[n];
            for (int i = 0; i < n; i++) {
                lst[i] = br.readLine();
            }

            Arrays.sort(lst);
            boolean flag = true;
            for (int j = 0; j < lst.length - 1; j++) {
                if (lst[j + 1].startsWith(lst[j])) {
                    System.out.println("NO");
                    flag = false;
                    break;
                }
                }
            if (flag) {
                System.out.println("YES");

            }
        }
    }
}
