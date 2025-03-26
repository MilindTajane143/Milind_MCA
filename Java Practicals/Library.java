import java.util.ArrayList;

class Library {
    private ArrayList<String> books;

    public Library() { books = new ArrayList<>(); }
    public void addBook(String book) { books.add(book); }
    public void removeBook(String book) { books.remove(book); }
    public void displayBooks() {
        System.out.println("Books in library: " + books);
    }

    public static void main(String[] args) {
        Library library = new Library();
        library.addBook("The Great Gatsby");
        library.addBook("1984");
        library.displayBooks();
        library.removeBook("1984");
        library.displayBooks();
    }
}
