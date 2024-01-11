package week2.day2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class B1759{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int l = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        char[] chars = new char[c];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < c; i++) {
            chars[i] = st.nextToken().charAt(0);

        }


    }
}
