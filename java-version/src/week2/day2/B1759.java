package week2.day2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class B1759{
    public static int L, C;
    public static char[] chars;
    public static char[] code;

    static void makeCode(int x, int idx) {
        if (idx == L) {
            if (isValid()) {
                System.out.println(code);
            }
            return;
        }

        //아직 L의 코드를 만들지 않았고 글자도 남았을경우
        for (int i = x; i < C; i++) {
            code[idx] = chars[i];
            makeCode(i+1, idx+1);
        }
    }

    static boolean isValid(){
        int cntC = 0;
        int cntV = 0;
        // 들어오는 문자의 자음 판단
        for (char x : code) {
            if (x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u') {
                cntV++;
            }else{
                cntC++;
            }
        }
        if (cntC >= 2 && cntV >= 1) {
            return true;
        }
        return false;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());


        chars = new char[C];
        code = new char[L];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < C; i++) {
            chars[i] = st.nextToken().charAt(0);
        }


        makeCode(0,0);

    }
}
