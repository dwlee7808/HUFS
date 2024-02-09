import java.io.*;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] arg)throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        
        String str = bf.readLine();
        StringTokenizer st = new StringTokenizer(str," ");
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        
        System.out.println(A+B);
        

    }
}