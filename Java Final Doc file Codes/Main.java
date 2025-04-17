import mymath.Complex;

public class Main {
    public static void main(String[] args) {
        // Creating array of Complex objects
        Complex[] numbers = new Complex[2];
        numbers[0] = new Complex(3, 4);
        numbers[1] = new Complex(1, 2);

        // Perform addition
        numbers[0].add(numbers[1]);

        System.out.println("After Addition:");
        numbers[0].display();
    }
}
