package grammer;

import java.util.HashMap;

public class hash {
    public static void main(String[] args) {


        HashMap<Integer, Integer> map = new HashMap<>();

        map.put(1,3);
        map.put(2,4);
        map.put(3,5);
        map.put(5,5);
        System.out.println(map);
        System.out.println(map.get(1));
        System.out.println(map);


        for(Integer i : map.keySet()){
            System.out.println(i+ "value"+map.get(i));
        }
    }
}