package week2.day5;

//https://www.acmicpc.net/problem/1244
//스위치 켜고 끄기


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1244 {
    static void changeArr(int stu, int num, int[] arr) {
        if (stu == 1) {
            for (int i = num; i < arr.length; i += num) {
                arr[i] = arr[i] == 0 ? 1 : 0;
            }
        } else if (stu == 2) {
            int left =num;
            int right = num;

            while (left > 0 && right < arr.length) {
                if (arr[left] != arr[right]) {
                    break;
                }
                left--;
                right++;

            }
            left++;
            right--;

            for (int i = left; i <= right; i++) {
                arr[i] = arr[i] == 0 ? 1 : 0;
            }
        }


    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int arr[] = new int[N+1];


        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i]= Integer.parseInt(st.nextToken());
        }




        int tc = Integer.parseInt(br.readLine());
        for (int i = 0; i < tc; i++) {
            st = new StringTokenizer(br.readLine());
            int stu = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());

            changeArr(stu, num, arr);
        }

        for (int i = 1; i < arr.length; i++) {
            System.out.print(arr[i]+" ");
            if (i % 20 == 0) {
                System.out.println();
            }
        }

    }


}

