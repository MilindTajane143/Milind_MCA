package mymath;

public class Complex {
    double real, imaginary;

    public Complex(double r, double i) {
        real = r;
        imaginary = i;
    }

    public void add(Complex num) {
        real = real + num.real;
        imaginary = imaginary + num.imaginary;
    }

    public void subtraction(Complex num) {
        real = real - num.real;
        imaginary = imaginary - num.imaginary;
    }

    public void multiplication(Complex num) {
        double tempReal = (real * num.real) - (imaginary * num.imaginary);
        double tempImaginary = (real * num.imaginary) + (imaginary * num.real);
        real = tempReal;
        imaginary = tempImaginary;
    }

    public void display() {
        System.out.println(real + " + " + imaginary + "i");
    }
}
