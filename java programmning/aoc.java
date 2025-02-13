import java.util.*;
public class aoc{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the radius of circle: ");
        float radius = sc.nextFloat();
        if (radius <=0){
            System.out.println("Radius can not be less tha 1 to calculate area of circle");
        }
        else
        {
            int nu=22, de=7;
            float area = (float)nu/de*radius*radius;
        System.out.println("Area of circle is " + area +" sq. units");
        }
    }
}