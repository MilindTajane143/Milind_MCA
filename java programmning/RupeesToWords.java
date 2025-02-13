import java.util.Scanner;
public class RupeesToWords {
    private static final String[] units = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                                           "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    private static final String[] tens = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    private static String convertToWords(int num) {
        if (num == 0) return "Zero";
        if (num < 20) return units[num];
        if (num < 100) return tens[num / 10] + (num % 10 != 0 ? " " + units[num % 10] : "");
        if (num < 1000) return units[num / 100] + " Hundred" + (num % 100 != 0 ? " " + convertToWords(num % 100) : "");
        return convertToWords(num / 1000) + " Thousand" + (num % 1000 != 0 ? " " + convertToWords(num % 1000) : "");
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter rupees: ");
        int rupees = scanner.nextInt();
        System.out.println("In words: " + convertToWords(rupees) + " Rupees");
    }
}