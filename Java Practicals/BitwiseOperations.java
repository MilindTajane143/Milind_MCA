import java.util.Scanner;

class BitwiseOperations {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter first integer: ");
        int num1 = scanner.nextInt();
        
        System.out.print("Enter second integer: ");
        int num2 = scanner.nextInt();
        
        System.out.println("Bitwise AND: " + (num1 & num2));
        System.out.println("Bitwise OR: " + (num1 | num2));
        System.out.println("Bitwise XOR: " + (num1 ^ num2));
        System.out.println("Bitwise Complement of first number: " + (~num1));
        System.out.println("Left Shift (num1 << 2): " + (num1 << 2));
        System.out.println("Right Shift (num1 >> 2): " + (num1 >> 2));
        
        scanner.close();
    }
}