package com.company;

import java.util.Scanner;
public class Bank_System {

    public static void main(String[] args) {
        Scanner entry = new Scanner(System.in);
        int user_entry;
        int size = 0;
        double[] acc_Bals = new double[100];
        String[] acc_names = new String[100];
        for(;true;) {
            System.out.println("");
            System.out.println("Bank Admin Menu:	");
            System.out.println("Please Enter a Menu Option");
            System.out.println("(1): Add Customer to Bank");
            System.out.println("(2): Change Customer Name");
            System.out.println("(3): Check Account Balance");
            System.out.println("(4): Modify Account Balance");
            System.out.println("(5): Summary of all Accounts");
            System.out.println("(-1): Exit");

            user_entry = entry.nextInt();

            if(user_entry == 1) {
                System.out.println("Bank Add Customer Menu:");
                System.out.println("Please Enter Account Balance");
                double bal = entry.nextDouble();
                acc_Bals[size] = bal;
                System.out.println("Please Enter Account name");
                entry.nextLine();
                String name = entry.nextLine();
                acc_names[size] = name;
                System.out.println("Your Customer_ID is " + size);
                size = size + 1;
            }
            else if(user_entry == 2) {
                System.out.println("Bank Change Name Menu:");
                System.out.println("Please Enter Customer_ID for changing the name");
                int c_id = entry.nextInt();
                System.out.println("Please Enter new Customer Name");
                entry.nextLine();
                acc_names[c_id] = entry.nextLine();


            }
            else if(user_entry == 3) {
                System.out.println("Bank Check Balance Menu:");
                System.out.println("Please Enter Customer_ID for checking Balance");
                int c_id = entry.nextInt();
                double bal = acc_Bals[c_id];
                System.out.println("You now have Rs." + bal + " in their account.");

            }
            else if(user_entry == 4) {
                System.out.println("Bank Modify Balance Menu:");
                System.out.println("Please Enter Customer_ID for modifying Balance");
                int c_id = entry.nextInt();
                System.out.println("Please Enter the below Menu Option:");
                System.out.println("(1): Withdraw Amount");
                System.out.println("(2): Deposit Amount");
                int input = entry.nextInt();
                if(input == 1) {
                    System.out.println("Please Enter Amount to Withdraw");
                    entry.nextLine();
                    double withdraw = entry.nextDouble();
                    if(withdraw <= acc_Bals[c_id]) {
                        acc_Bals[c_id] = acc_Bals[c_id] - withdraw;
                    }
                    else{
                        System.out.println("Sorry! Your Bank do not have the requested amount to be withdrawn");
                    }
                }
                else if(input == 2) {
                    System.out.println("Please Enter Amount to Deposit");
                    entry.nextLine();
                    double deposit = entry.nextDouble();
                    acc_Bals[c_id] = acc_Bals[c_id] + deposit;
                }
                double bal = acc_Bals[c_id];
                System.out.println("This Customer has Rs." + bal + " in their account.");

            }
            else if(user_entry == 5) {
                System.out.println("Bank All Customer Summary Menu:");
                double total = 0;
                for(int i = 0; i < size; i++) {
                    total = total + acc_Bals[i];
                    System.out.println("Name of the Customer: " + acc_names[i] + "	&	Balance of the Customer: " + acc_Bals[i]);
                    System.out.println("THe Bank has total Rs." + total + " in it's accounts.");
                }

            }
            else if(user_entry == -1) {
                System.exit(-1);
            }
            else {
                System.out.println("ERROR! Please Enter a valid Input:");
            }
        }
    }
}
