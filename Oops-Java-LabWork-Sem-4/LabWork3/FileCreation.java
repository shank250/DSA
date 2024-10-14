import java.util.*;
import java.io.File;
import java.io.IOException;
public class FileCreation{
        public static void main(String[] args){
            File fileObj = new File("D:/DSA/JavaOops/LabWork3/testFileCreation.txt");
            try{
                if (fileObj.createNewFile()){
                    System.out.println("File Created!");
               }else{
                    System.out.println("Failure while creatinf a new file.!");
                }
            }
            catch (IOException e){
                System.out.println("Exception occured.");
            }
            
        }
}
