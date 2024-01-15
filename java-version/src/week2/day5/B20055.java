package week2.day5;
//https://www.acmicpc.net/problem/20055
//컨베이어 벨트위의 로봇


//우선 한칸 이동  이동할때 로봇이 있으면 그로봇도 한칸이동
//로봇이 마지막 지점에 있으면 로봇 제거

// 가장 먼저 올라간 로봇 순서대로 한칸 더 이동할수있으면 이동
//이동후 수명1감소
//로봇이 마지막지점에 온다면 제거

//시작지점에 로봇을 올릴수있으면 올려라

// 내구도가 0개가 k개 이상이면 종료

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B20055 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] belt = new int[N*2];
        boolean[] robot = new boolean[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N*2; i++) {
            belt[i] = Integer.parseInt(st.nextToken());     // 컨베이어 벨트의 내구도를 입력받아 배열에 저장합니다.

        }

        int level = 0;     // 진행 단계를 나타내는 변수입니다.


        while(true) {
            level++;          // 레벨을 1 증가시킵니다.
            // 1단계
            int tmp = belt[N*2-1];
            for (int i = N*2-1; i > 0; i--) {
                belt[i] = belt[i-1];
            }         // 로봇도 한 칸 이동시킵니다.

            belt[0] = tmp;

            for (int i = N-1; i > 0; i--) {
                robot[i] = robot[i-1];
            }

            robot[0] = false;
            robot[N-1] = false;

            // 2단계
            for (int i = N-1; i > 0; i--) {
                if(robot[i-1] && !robot[i] && belt[i]>0) {
                    robot[i-1] = false;
                    robot[i] = true;
                    belt[i]--;
                    robot[N-1] = false;
                }
            }

            // 3단계
            if(belt[0]>0) {
                robot[0] = true;
                belt[0]--;
            }

            // 4단계
            int cnt = 0;
            for (int i = 0; i < N*2; i++) {
                if(belt[i] == 0) cnt++;
            }
            if(cnt>=K) break;

        }

        System.out.println(level);
    }
}
