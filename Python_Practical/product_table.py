from pymongo import MongoClient

# Establish connection to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
db = client["productdb"]  # Database name
product_collection = db["product"]  # Collection name

# Function to insert a product record
def insert_product():
    pid = input("Enter product ID: ")
    pname = input("Enter product name: ")
    price = float(input("Enter product price: "))
    product = {"pid": pid, "pname": pname, "price": price}
    product_collection.insert_one(product)
    print("Product inserted successfully.")

# Function to update product price
def update_price():
    pid = input("Enter product ID to update: ")
    new_price = float(input("Enter new price: "))
    result = product_collection.update_one({"pid": pid}, {"$set": {"price": new_price}})
    if result.matched_count > 0:
        print("Price updated successfully.")
    else:
        print("Product ID not found.")

# Function to delete a product by ID
def delete_product():
    pid = input("Enter product ID to delete: ")
    result = product_collection.delete_one({"pid": pid})
    if result.deleted_count > 0:
        print("Product deleted successfully.")
    else:
        print("Product ID not found.")

# Function to display all products
def display_all():
    products = product_collection.find()
    print("\n--- Product List ---")
    for product in products:
        print(f"ID: {product['pid']}, Name: {product['pname']}, Price: {product['price']}")
    print("---------------------")

# Menu-driven program
def main():
    while True:
        print("\n--- Product Management ---")
        print("1. Insert a record")
        print("2. Update price")
        print("3. Delete by PID")
        print("4. Display all products")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            insert_product()
        elif choice == "2":
            update_price()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            display_all()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
