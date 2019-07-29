
import java.util.Base64;

public class Main {

    public static void main(String[] args) {
        Base64.Encoder enc = Base64.getEncoder();
        Base64.Decoder dec = Base64.getDecoder();
        String str = "hello,wer,[1,2,3]";
        String encoded = enc.encodeToString(str.getBytes());
        System.out.println("encoded value is \t" + encoded);

        String decoded = new String(dec.decode(encoded));
        System.out.println("decoded value is \t" + decoded);
        String[] values = str.split(",");
        System.out.println("original value is \t" + values[2]);
    }

}
