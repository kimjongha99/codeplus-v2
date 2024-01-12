package week2.day3;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
//https://www.acmicpc.net/problem/1068

// 트리

public class B1068 {
    static List<List<Integer>> tree = new ArrayList<>();
    static boolean[] deleted;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt(); // Number of nodes

        for (int i = 0; i < N; i++) {
            tree.add(new ArrayList<>());
        }

        int root = 0;

        for (int i = 0; i < N; i++) {
            int parent = scanner.nextInt();
            if (parent != -1) {
                tree.get(parent).add(i);
            } else {
                root = i;
            }
        }

        int nodeToDelete = scanner.nextInt();
        deleted = new boolean[N];
        deleteNode(nodeToDelete);

        int leafCount = countLeaves(root);
        System.out.println(leafCount);
    }

    private static void deleteNode(int node) {
        deleted[node] = true;
        for (int child : tree.get(node)) {
            deleteNode(child);
        }
    }

    private static int countLeaves(int node) {
        if (deleted[node]) return 0;
        List<Integer> children = tree.get(node);
        if (children.isEmpty()) return 1;

        int leafCount = 0;
        for (int child : children) {
            leafCount += countLeaves(child);
        }
        return leafCount;
    }
}
