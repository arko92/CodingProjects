/*
ETL: Extract , Transform & Load
*/
#include "ETL.h"

#include <fstream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <cmath>
#include <boost/algorithm/string.hpp>

// Reads a CSV file and stores the data into a 2D vector

std::vector<std::vector<std::string>> ETL::readCSV()  // Returns a 2D vector
{

	std::ifstream file(Dataset); // reading the CSV file

	std::vector<std::vector<std::string>> dataString;  // A 2d (string) vector to store data from the file

	std::string line = "";

	while (getline(file, line)) { // Iterates through each line in the file

		std::vector<std::string> row_vec; // 1D vector to store data retrieved from each line

		boost::algorithm::split(row_vec, line, boost::is_any_of(Delimiter)); // Splits the line using delimiter

		dataString.push_back(row_vec);
	}

	file.close();

	return dataString;
}


Eigen::MatrixXd ETL::CSVtoEigen(std::vector<std::vector<std::string>> Dataset, int rows, int cols) {

	if (Header = true) {
		rows = rows - 1;

	}

	Eigen::MatrixXd mat(cols,rows);
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; ++j) {

			mat(j,i) = atof(Dataset[i][j].c_str());  // atof() -- converts strings to float; c_str() -- convert a given string to an array of characters
		}
		

	}
	return mat.transpose();
}
