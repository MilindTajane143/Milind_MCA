import java.util.ArrayList;
import java.util.Scanner;

public class ReplaceSecondElement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<>();
        System.out.print("Enter number of elements in ArrayList: ");
        int n = sc.nextInt();
        sc.nextLine();
        System.out.println("Enter " + n + " elements:");
        for (int i = 0; i < n; i++) {
            list.add(sc.nextLine());
        }
        if (list.size() >= 2) {
            System.out.print("Enter element to replace second element: ");
            String newElement = sc.nextLine();
            list.set(1, newElement);
            System.out.println("Updated ArrayList: " + list);
        } else {
            System.out.println("ArrayList must have at least 2 elements.");
        }
        sc.close();
    }
}