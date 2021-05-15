package Variables;

public class VarBasics_01 {
    public static void main(String[] args){

        //ANYTHING WITH TWO SLASHES IN FRONT OF IT IS A COMMENT AND CAN BE IGNORED

        //Decalaration
        String myString;

        //Assignment
        myString = "This is a string.";

        //different types of vars
        byte    myByte = 2;
        int     myInt = 32000;
        long    myLong = -2147483648;

        double  myDouble = 3.1415;

        char    myChar = 'c';

        boolean myBool = false;
        boolean myTrueBool; //booleans automatically initialize to true once declared in java

        //notice how String is capital but the rest are not!
        String  myNewString = "This is another string";

        //strings, chars, etc can be set to null to be empty (as there is no 0)
        String  myEmptyString = null;

        //No Null with numeric vars
        int     myEmptyNumber = 0;

        //myEmptyNumber = null; //error when set to null
    }
}
