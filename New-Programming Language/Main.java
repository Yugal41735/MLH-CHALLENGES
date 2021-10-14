package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
//        Output
//        System.out.print("Hello World!");
////        if we dont want a new line then instead of println we can use print only
//        System.out.println("My name is Yugal.");

//        Input
        Scanner input = new Scanner(System.in);
//        In above line we created an input variable of type scanner
//        System.in means we are taking input from the keyboard
//        System.out.println(input.nextInt());
//        the above will take int as input
//        System.out.println(input.next());
//        Even if we enter a whole sentence it will just take first string as a input
        System.out.println(input.nextLine());
    }
}
