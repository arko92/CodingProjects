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

		std::vector<std::string> row_vec; // 1D vector to store data in each line

		boost::algorithm::split(row_vec, line, boost::is_any_of(Delimiter)); // Splits the line using delimiter

		dataString.push_back(row_vec);
	}

	file.close();

	return dataString;
}
