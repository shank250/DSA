import java.io.FileWriter;

public class WirtingIntoFile{
    public static void main(String[] args){
        try{
            FileWriter file = new FileWriter("D:/DSA/JavaOops/LabWork3/testFileCreation.txt");
            file.write("Hello world!"); 
            file.close();
            System.out.println("Written successfully!");
        }
        catch(Exception e){
            System.out.println("Error");
            e.printStackTrace();
        }
    }
}