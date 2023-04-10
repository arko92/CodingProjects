#pragma once

#ifndef ETL_h
#define ETL_h

#include<iostream>;
#include<vector>;


class ETL {

	std::string Dataset;  // Dataset file name
	std::string Delimiter;   // Type of delimiter used in the data set 
	bool Header; // To check if any header row is present

public:
	// Constructor

	ETL(std::string dataset, std::string delimiter, bool header) {

		Dataset = dataset;
		Delimiter = delimiter;
		Header = header;
	}

	std::vector<std::vector<std::string>> readCSV(); // Reads a CSV file and stores the data into a 2D vector

};

#endif
