import java.io.*;

class SharedData {
    String line;
    boolean hasData = false;

    // Writer waits until reader puts data
    public synchronized void write(String line) {
        while (hasData) {
            try {
                wait();
            } catch (InterruptedException e) {
            }
        }
        this.line = line;
        hasData = true;
        notify();
    }

    // Reader waits until writer reads data
    public synchronized String read() {
        while (!hasData) {
            try {
                wait();
            } catch (InterruptedException e) {
            }
        }
        hasData = false;
        notify();
        return line;
    }
}

class ReaderThread extends Thread {
    SharedData data;
    BufferedReader br;

    ReaderThread(SharedData data, String inputFile) throws IOException {
        this.data = data;
        br = new BufferedReader(new FileReader(inputFile));
    }

    public void run() {
        try {
            String line;
            while ((line = br.readLine()) != null) {
                data.write(line); // Send to writer
            }
            data.write("EOF"); // End marker
            br.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

class WriterThread extends Thread {
    SharedData data;
    BufferedWriter bw;

    WriterThread(SharedData data, String outputFile) throws IOException {
        this.data = data;
        bw = new BufferedWriter(new FileWriter(outputFile));
    }

    public void run() {
        try {
            String line;
            while (!(line = data.read()).equals("EOF")) {
                bw.write(line);
                bw.newLine();
            }
            bw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

public class SimpleFileCopySync {
    public static void main(String[] args) {
        try {
            SharedData shared = new SharedData();
            // Change these to your actual file paths
            ReaderThread reader = new ReaderThread(shared, "input.txt");
            WriterThread writer = new WriterThread(shared, "output.txt");
            reader.start();
            writer.start();
            reader.join();
            writer.join();
            System.out.println("File copied successfully using synchronized threads!");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}