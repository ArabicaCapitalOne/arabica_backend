#include <iostream>
#include <cstdlib>
#include <vector>
#include <fstream>
#include <cstdio>

using namespace std;

void output(int year, int month, int day, vector<string> &merchant_id) {
	cout << "{\n";
	int index = rand() % 300;
	cout << " \"merchant_id\": " << "\"" << merchant_id[index] << "\"," << endl;
	cout << " \"medium\": " << "\"balance\"," << endl;
	printf(" \"purchase_date\": \"%d-%02d-%02d\",\n", year, month, day);
	// cout << " \"purchase_date\": " << "\"" << year << "-" << month << "-" << day << "\",\n";
	int a = rand() % 50;
	int b = rand() % 10;
	int c = rand() % 10;
	cout << " \"amount\": " << a << "." << b << c << ",\n";
	cout << " \"description\": " << "\"string\"\n";
	cout << "},\n\n";
}



int main (){

	vector<string> merchant_id;
	ifstream fin("test.txt");
	string id;
	while (fin >> id) {
		merchant_id.push_back(id);
	}


	for (int year = 2012; year < 2017; ++year) {
		for (int month = 1; month <= 12; ++month) {
			int num = rand() % 50 + 10;
			for (int count = 0; count < num; ++count) {
				int day = 0;
				if (month == 2)
					day = rand() % 28 + 1;
				else if (month==4 || month==6 || month==9 || month==11)
					day = rand() % 30 + 1;
				else
					day = rand() % 31 + 1;
				output (year, month, day, merchant_id);
			}
		}
	}

	return 0;
}
