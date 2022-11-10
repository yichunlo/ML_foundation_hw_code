#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#define theta first
#define s second

using namespace std;

const int size = 2000;

inline int sign(double x){
	return (x > 0)? 1 : -1;
}

struct data{
	double x[size+12];
	int y[size+12];
}Data;

pair<double, int> hypo, best;

void gen_data(){
	for(int i = 0; i < size; i++)
		Data.x[i] = 2.0 * rand() / double(RAND_MAX) - 1.0;
	sort(Data.x, Data.x+size);
	for(int i = 0; i < size; i++){
		Data.y[i] = sign(Data.x[i]);
		double r = rand() / double(RAND_MAX);
		if(r < 0.2) Data.y[i] *= -1;
	}
}

inline double err_rate(){
	int sum = 0;
	for(int i = 0; i < size; i++)
		if(hypo.s * sign(Data.x[i] - hypo.theta) != Data.y[i]) sum++;
	return sum / double(size);
}

double Ein(){
	double min_err_rate = 1.0;
	int s = -1;
	while(s <= 1){
		hypo.s = s;
		for(int i = 0; i <= size; i++){
			if(i == 0) hypo.theta = Data.x[0] - 1.0;
			if(i == size) hypo.theta = Data.x[size-1] + 1.0;
			else hypo.theta = (Data.x[i-1] + Data.x[i]) / 2.0;
			double err = err_rate();
			if(err < min_err_rate){
				best = hypo;
				min_err_rate = err;
			}
		}
		s += 2;
	}
	return min_err_rate;
}

int main(){
	srand(time(NULL));
	double sum1 = 0, sum2 = 0;
	for(int i = 0; i < 1000; i++){
		gen_data();
		double min_err = Ein();
		sum1 += min_err;
		sum2 += (0.5 + 0.3 * double(best.s) * (double)(fabs(best.theta)-1.0));
		cout << min_err - (0.5 + 0.3 * double(best.s) * (double)(fabs(best.theta)-1.0)) << '\n';
	}
	cerr << "Ein average = " << sum1 / double(1000) << " Eout average = " << sum2 / double(1000) << '\n';
	return 0;
}
