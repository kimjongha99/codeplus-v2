package week3.day1;
//https://www.acmicpc.net/problem/10814

//나이순 정렬

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class B10814 {
  static  class person{
        int age;
        String name;
        int count;

        public person(int age, String name, int count) {     // 생성자: person 객체를 생성할 때 나이, 이름, 카운트 값을 초기화합니다.

            this.age = age;
            this.name = name;
            this.count = count;
        }
    }
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<person> people = new ArrayList<>();     // person 객체를 저장할 ArrayList를 생성합니다.

        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            int age = Integer.parseInt(input[0]);
            String name = input[1];
            people.add(new person(age, name, i));  // 입력받은값을 추가.
        }

        Collections.sort(people, new Comparator<person>() {   // Collections.sort를 사용하여 people 리스트를 정렬합니다.

            @Override
            public int compare(person o1, person o2) {
                // 나이가 같다면 등록 순서(count)로 비교합니다.
                if (o1.age == o2.age) {
                    return Integer.compare(o1.count, o2.count);
                }
                // 나이가 다르면 나이로 비교합니다.
                return Integer.compare(o1.age, o2.age);
            }
        });

        for (int i = 0; i < people.size(); i++) {
            person ans = people.get(i);
            System.out.println(ans.age+" "+ans.name);
        }
    }

}
