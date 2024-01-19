package week3.day3;
//https://www.acmicpc.net/problem/2512
//예산

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;



public class B2512 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int [] arr =new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int m = Integer.parseInt(br.readLine());


        Arrays.sort(arr);

        int start =0;
        int end = arr[n - 1];

        int result =0;

        while (start <= end) { // 시작보다 end가 커지면 종료
            int mid = (start+end)/2;
            int sum =0;

            for (int i = 0; i < n; i++) {
                if (arr[i] > mid) {  // 예산을 초과하지않으면서 가능한 최대로 할당해야하기때문에
                                     // 현재 예산 상한액보다 ar[i]가 크다면 그지방에는 mid만큼할당해야합니다.
                    sum += mid;
                }else {
                    sum +=arr[i]; // 그게아니라면 지금 arr[i]의 금액만큼할당합니다
                }
            }

            if (sum > m) {    //만약 총 에산액이 m보다 크다면  상한값이 너무 크다는의미로 mid에 1을 줄여서 범위를 좁히고
                end = mid-1;
            }else{    //반대로 sum이 m 이하라면, 현재의 mid는 유효한 상한액이며, 더 큰 상한액을 시도할 수 있도록 start를 mid+1로 증가시킵니다. 또한, 현재의 mid가 유효한 상한액임을 확인했으므로, 결과값을 Math.max(result, mid)로 업데이트하여 지금까지 확인한 상한액 중 최대값을 유지합니다.
                start = mid+1;
                result = Math.max(result, mid);
            }

        }

        System.out.println(result);

    }
}
