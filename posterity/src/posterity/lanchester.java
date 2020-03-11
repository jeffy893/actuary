package posterity;
import java.util.ArrayList;

import Jama.Matrix;

public class lanchester {
	
	double this_a = 1.0;
	double this_b = 1.0;
	double this_c = 1.0;
	double this_d = 1.0;
	double this_e = 1.0;
	double this_f = 1.0;
	double xprime = 1.0;
	double yprime = 1.0;
	int this_intervals = 1;
	double this_size = 3.0;
	ArrayList<Double[]> graph = new ArrayList<Double[]>();
	
	
	public lanchester(double size,int intervals, double a, double b, double c, double d, double e, double f) {
		
		this_a = a;
		this_b = b;
		this_c = c;
		this_d = d;
		this_e = e;
		this_f = f;
		this_intervals = intervals;
		this_size = size;
		
		
		
	}
	
	
	public ArrayList<Double[]> getGraph(){
		return graph;
	}
	
	public static int factorial(int k) {
		
		int n = 1;
		
		if(k == 0) {
			return n;
		}else {
			
			while(k > 0) {
				n = n * k;
				k = k - 1;
			}
			
			return n;
		}
		
		
		
	}
	
	
	
	public ArrayList<Double[]> setPossible(Matrix bdchain, double num_people, double flux_people, double cohdelta, double forcedelta){
		
		double max = 0.000001;
		for(int i = 0; i < this_intervals-2; i++) {
			
			//statistics on the battles divided by the all_comb
			if(max < bdchain.get(i, 0)) {
				max = bdchain.get(i, 0);
			}
			
		}
		
		double value = 1.0;
		
		
		
		
		for(int i = 0; i < this_intervals-2; i++) {
			
			if(bdchain.get(i, 0) < max) {
				
				this_e = this_size/6;
				if(flux_people/num_people > (this_size/3)) {
					this_c = this_size/3;
				}else {
					this_c = flux_people/num_people;
				}
				
				this_a = (bdchain.get(i, 0)/max)*(this_size/6);
				
				
				for(int j = 0; j < this_intervals; j++) {
					this_f = this_f + forcedelta;	
					battle();
				}
				
				
			}else if (bdchain.get(i,0) > max) {
				
				this_a = this_size/6;
				if(flux_people/num_people > (this_size/3)) {
					this_f = this_size/3;
				}else {
					this_f = flux_people/num_people;
				}
				
				this_e = (bdchain.get(i, 0)/max)*(this_size/6);
				
				
				for(int j = 0; j < this_intervals; j++) {
					this_c = this_c + forcedelta;
					battle();
				}
				
				
				
			}
			
			
		}
		
		
		
		
		
		for(int i = 0; i < this_intervals-2; i++) {
			
		}
		
		
		
		
		return graph;
		
	}
	
	
	public void battle() {
		
		
		int N = this_intervals;
		Double[] X = new Double[N+1];
		Double[] Y = new Double[N+1];

		X[0] = this_size;
		Y[0] = this_size;

		double dt = 4.0 / N;

		for (int i = 0; i < 100; ++i)
		{
		   double t = i*dt;

		   /* calculate derivatives */
		   xprime = - this_a * X[i] * Y[i] - this_b * Y[i] + this_c*Math.cos(t) + this_c*t;
		   yprime = - this_d * X[i]  - this_e  * X[i] * Y[i] + this_f*Math.cos(t) + this_f*t;

		   /* now integrate using Euler */
		   X[i+1] = X[i] + xprime * dt;
		   Y[i+1] = Y[i] + yprime * dt;
		   
		}
		
		graph.add(X);
		graph.add(Y);
	}
	
}
