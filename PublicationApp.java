import java.util.Scanner;

/**
 * Base class for anything the company publishes.
 */
class Publication {
    private String title;
    private double price;

    // Simple method to store the publication's core data
    public void set(String title, double price) {
        this.title = title;
        this.price = price;
    }
    
    // A quick way to see the core data
    public void display() {
        System.out.println("\n-- Publication Details --");
        System.out.println("Title: " + title);
        System.out.println("Price: $" + String.format("%.2f", price));
    }
}

/**
 * Represents a physical book.
 */
class Book extends Publication {
    private int pageCount;

    // Overloaded set method to handle the extra book-specific detail
    public void set(String title, double price, int pageCount) {
        super.set(title, price); // Set the title and price first
        this.pageCount = pageCount;
    }
    
    @Override
    public void display() {
        super.display(); // Show the title and price
        System.out.println("Type: Book");
        System.out.println("Pages: " + pageCount);
    }
}

/**
 * Represents an audio cassette (Tape).
 */
class Tape extends Publication {
    private int playingTimeMinutes;

    // Overloaded set method to handle the extra tape-specific detail
    public void set(String title, double price, int playingTimeMinutes) {
        super.set(title, price); // Set the title and price first
        this.playingTimeMinutes = playingTimeMinutes;
    }

    @Override
    public void display() {
        super.display(); // Show the title and price
        System.out.println("Type: Audio Tape");
        System.out.println("Playing Time: " + playingTimeMinutes + " minutes");
    }
}

// Main application class
public class PublicationApp {
    public static void main(String[] args) {
        Scanner userInput = new Scanner(System.in);
        
        // Prepare objects for the book and tape
        Book newBook = new Book();
        Tape newTape = new Tape();

        // --- Get Book Details from User ---
        System.out.println("--- Enter Book Details ---");
        System.out.print("Title: ");
        String bookTitle = userInput.nextLine();
        System.out.print("Price ($): ");
        double bookPrice = userInput.nextDouble();
        System.out.print("Number of pages: ");
        int pages = userInput.nextInt();
        userInput.nextLine(); // Clear the buffer after reading the number

        // Store the book data
        newBook.set(bookTitle, bookPrice, pages);

        // --- Get Tape Details from User ---
        System.out.println("\n--- Enter Audio Tape Details ---");
        System.out.print("Title: ");
        String tapeTitle = userInput.nextLine();
        System.out.print("Price ($): ");
        double tapePrice = userInput.nextDouble();
        System.out.print("Playing time (minutes): ");
        int playingTime = userInput.nextInt();
        userInput.nextLine(); // Clear the buffer

        // Store the tape data
        newTape.set(tapeTitle, tapePrice, playingTime);

        // --- Display Results ---
        System.out.println("\n=================================");
        System.out.println("Showing Stored Publication Details:");
        
        newBook.display();
        
        System.out.println("---------------------------------");

        newTape.display();

        userInput.close();
    }
}