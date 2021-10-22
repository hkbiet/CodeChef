# include <iostream>
#include <string>
#include <unordered_set>
#include <limits>
#include <cstdlib>
using namespace std;


void solve(){

		int total_money;

	cin>>total_money;


		if(total_money == 1){
		cout<<"1 0"<<"\n";
		return;}
	int Q, R, Q_major, R_major,diff, temp_diff;
	Q = total_money / 2;
	R = 0;
	Q_major = 0;
	R_major = 0;
	diff = std::numeric_limits<int>::max();


		while(Q){
		R = total_money - (2 * Q);
		temp_diff = abs(Q-R);

		if(temp_diff < diff ){
			diff = temp_diff;
			Q_major = Q;
			R_major = R;
			Q = Q - 1;}
		else if (temp_diff > diff){
			cout<<R_major<<" "<<Q_major<<"\n";
			return;}
		else{
			Q = Q - 1;
		}
	}
	return;



	




}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	int t;
	cin>>t;
	while(t--){
        solve();
    }
	return 0;
}