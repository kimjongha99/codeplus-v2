package week3.day1;

//https://www.acmicpc.net/problem/2108
//통계학


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class B2108 {
    static  int N;
    static void func1(List<Integer> list){
        double sum =0;
        for (int i : list) {
            sum+=i;
        }
        System.out.println(Math.round(sum / N));
    }
    static void func2(List<Integer> list) {
        int mid = list.size()/2;
        System.out.println(list.get(mid));

    }

    static void func3(List<Integer> list) {
        int[] counts = new int[8001];

        for (int number : list) {
            counts[number + 4000]++;
        }
        int maxCount = 0;
        // 최대 빈도수 찾기
        for (int count : counts) {
            if (count > maxCount) {
                maxCount = count;
            }
        }
        List<Integer> modes = new ArrayList<>();
        for (int i = 0; i < counts.length; i++) {
            if (counts[i] == maxCount) {
                modes.add(i - 4000); // 원래 숫자로 변환
            }
        }
        Collections.sort(modes); // 정렬

        if (modes.size() == 1) {      // 최빈값이 하나만 있는 경우 혹은 두 번째로 작은 최빈값을 출력
            System.out.println(modes.get(0));
        } else {
            System.out.println(modes.get(1));
        }


    }

    static void func4(List<Integer> list) {
        int first = list.get(0);
        int end = list.get(list.size() - 1);
        System.out.println(end - first);
    }
        public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            list.add(Integer.parseInt(br.readLine()));
        }
        Collections.sort(list);

        func1(list);
        func2(list);
        func3(list);
        func4(list);

    }
}
