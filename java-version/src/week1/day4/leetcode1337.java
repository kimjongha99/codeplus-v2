package week1.day4;
//https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/
//        2차원 배열에서의 1은 군인  0 은 민간인
//        행렬에서  한 행의 군인의 수 얼마나 많은지

import java.util.*;

public class leetcode1337 {
    public int[] kWeakestRows(int[][] mat, int k) {
        HashMap<Integer,Integer> map = new HashMap<>();

        for (int i = 0; i < mat.length; i++) {
            int count =0;
            for (int j = 0; j < mat[0].length; j++) {
                if(mat[i][j]==1){
                    count++;
                }
            }
            map.put(i,count);
        }
        System.out.println(map);// 해쉬맵에 군인이개수 저장 콘솔


        List<Integer> list = new ArrayList<>(map.keySet());
        Collections.sort(list, (a, b) -> map.get(a) - map.get(b));
        //map.get(a) - map.get(b):
        //map은 키가 행 인덱스이고 값이 해당 행에 있는 군인 수인 HashMap입니다.
        //map.get(a)는 a 행의 군인 수를 가져옵니다.
        //map.get(b)는 b 행의 군인 수를 가져옵니다.
        //map.get(a) - map.get(b)는 a 행과 b 행 사이의 군인 수 차이를 계산합니다.

        int[] ans = new int[k];
        for (int i = 0; i < k; i++) {
            ans[i] = list.get(i);
        }

        return ans;

    }

    public static void main(String[] args) {
        leetcode1337 sol = new leetcode1337();
        int[][] mat = {
                {1, 0, 0, 0},
                {1, 1, 1, 1},
                {1, 0, 0, 0},
                {1, 0, 0, 0}
        };
        int k = 2;
        int[] result = sol.kWeakestRows(mat, k);
        System.out.print("Output: ");
        for (int i : result) {
            System.out.print(i + " ");
        }
    }
}
