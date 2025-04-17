import java.util.Scanner;

class Temp {
    public static void main(String[] args) {
        float celsius, fahrenheit;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Celsius value to convert to Fahrenheit: ");
        celsius = sc.nextFloat();
        fahrenheit = (celsius * 9 / 5) + 32;
        System.out.println("The converted temperature in Fahrenheit is: " + fahrenheit);
        System.out.println("Enter the Fahrenheit value to convert to Celsius: ");
        fahrenheit = sc.nextFloat();
        celsius = (fahrenheit - 32) * 5 / 9;
        System.out.println("The converted temperature in Celsius is: " + celsius);
        sc.close();
    }
}
