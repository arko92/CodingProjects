// calculator.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include "functions.h"
using namespace std;

int main()
{
    float num1, num2;
    string operations[3] = { "add","substract","multiply" };
    string operation;
    
    cout << "----- Simple Calculator -------" << endl;
    
    cout << "Enter two numbers: " << endl;

    cin >> num1;
    cin >> num2;

    cout << "Available operations: " << endl;
    
    for (int i = 0; i < size(operations); i++) {
        cout << operations[i] << endl;
    }

    cout << "Type an operation: " << endl;

    cin >> operation;

    cout << "Selected operation: " <<operation<< endl;

    if (operation == "add") {
        cout <<"Result: "<<add(num1,num2) << endl;
    } 
    else if (operation == "substract") {
        cout <<"Result: "<< substract(num1,num2) << endl;
    } 
    else if (operation == "multiply") {
        cout <<"Result: "<< multiply(num1,num2) << endl;

    }
    else {
        cout << "operation not found. Please enter a valid operation" << endl;

    }

}













// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
