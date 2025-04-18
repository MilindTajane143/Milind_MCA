import java.util.Scanner;

interface VehicleInfo {
    void displayInfo();
}

class Vehicle implements VehicleInfo {
    String company;
    double price;

    public Vehicle(String company, double price) {
        this.company = company;
        this.price = price;
    }

    @Override
    public void displayInfo() {
        System.out.println("Company: " + company);
        System.out.println("Price: " + price);
    }
}

class LightMotorVehicle extends Vehicle {
    double mileage;

    public LightMotorVehicle(String company, double price, double mileage) {
        super(company, price);
        this.mileage = mileage;
    }

    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Mileage: " + mileage + " km/l");
    }
}

class HeavyMotorVehicle extends Vehicle {
    double capacityInTons;

    public HeavyMotorVehicle(String company, double price, double capacityInTons) {
        super(company, price);
        this.capacityInTons = capacityInTons;
    }

    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Capacity: " + capacityInTons + " tons");
    }
}

public class VehicleDemo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of vehicles: ");
        int n = scanner.nextInt();
        scanner.nextLine();
        Vehicle[] vehicles = new Vehicle[n];
        for (int i = 0; i < n; i++) {
            System.out.println("\nEnter information for Vehicle " + (i + 1));
            System.out.print("Enter vehicle type (1 for LightMotorVehicle, 2 for HeavyMotorVehicle): ");
            int vehicleType = scanner.nextInt();
            scanner.nextLine();
            System.out.print("Enter company name: ");
            String company = scanner.nextLine();
            System.out.print("Enter price of vehicle: ");
            double price = scanner.nextDouble();
            scanner.nextLine();
            if (vehicleType == 1) {
                System.out.print("Enter mileage (in km/l): ");
                double mileage = scanner.nextDouble();
                vehicles[i] = new LightMotorVehicle(company, price, mileage);
            } else if (vehicleType == 2) {
                System.out.print("Enter capacity in tons: ");
                double capacityInTons = scanner.nextDouble();
                vehicles[i] = new HeavyMotorVehicle(company, price, capacityInTons);
            } else {
                System.out.println("Invalid vehicle type! Please enter 1 or 2.");
                i--;
            }
            scanner.nextLine();
        }
        System.out.println("\nVehicle Information:");
        for (int i = 0; i < n; i++) {
            System.out.println("\nVehicle " + (i + 1) + " details:");
            vehicles[i].displayInfo();
        }
        scanner.close();
    }
}