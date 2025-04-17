import java.util.Scanner;

class AreaOfCircle {
    public static void main(String[] args) {
        int n = 22, d = 7;
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter radius: ");
        double r = sc.nextDouble();
        if (r > 0) {
            // Using type casting for accurate result
            double area = (double) n / d * r * r;
            System.out.println("Area of circle: " + area);
        } else {
            System.out.println("Invalid input. Radius should be greater than zero.");
        }
        sc.close();
    }
}