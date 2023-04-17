/*

Description:
This is a simple linear regression fit program which does the following :
1. Reads data from a .csv file
2. Fits a linear regression function to it
3. Plots the result

*/

// Necessary libraries

#include "ETL/ETL.h"

#include <iostream>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include<Eigen/Dense>

using namespace std;


int main(int argc, char* argv[]) {

	//ETL etl(argv[1], argv[2], argv[3]);

	ETL etl("Anscombes-quartet-data.csv", ",", true); // Creating an instance of ETL and initializing it

	std::vector<std::vector<std::string>> data = etl.readCSV();

	int rows = data.size();

	int cols = data[0].size();

	Eigen::MatrixXd Mat = etl.CSVtoEigen(data,rows,cols);

	std::cout << Mat << std::endl;

	return EXIT_SUCCESS;

}




