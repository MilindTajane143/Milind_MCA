import java.text.DecimalFormat;

class NumberToWords {
    private static final String[] units = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    private static final String[] tens = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};

    public static String convert(int number) {
        if (number == 0) return "Zero";
        return convertNumberToWords(number);
    }

    private static String convertNumberToWords(int number) {
        if (number < 20) return units[number];
        if (number < 100) return tens[number / 10] + (number % 10 != 0 ? " " + units[number % 10] : "");
        if (number < 1000) return units[number / 100] + " Hundred" + (number % 100 != 0 ? " " + convertNumberToWords(number % 100) : "");
        if (number < 100000) return convertNumberToWords(number / 1000) + " Thousand" + (number % 1000 != 0 ? " " + convertNumberToWords(number % 1000) : "");
        if (number < 10000000) return convertNumberToWords(number / 100000) + " Lakh" + (number % 100000 != 0 ? " " + convertNumberToWords(number % 100000) : "");
        return convertNumberToWords(number / 10000000) + " Crore" + (number % 10000000 != 0 ? " " + convertNumberToWords(number % 10000000) : "");
    }

    public static void main(String[] args) {
        int amount = 230020;
        System.out.println("Rupees " + new DecimalFormat("#,##0").format(amount) + " in words: " + convert(amount) + " Rupees");
    }
}