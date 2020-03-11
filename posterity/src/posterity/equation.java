package posterity;

import java.util.ArrayList;

public class equation {
	
	double this_a = 1.0;
	double this_b = 1.0;
	double this_c = 1.0;
	double this_d = 1.0;
	double this_e = 1.0;
	double this_f = 1.0;
	double xprime = 1.0;
	double yprime = 1.0;
	ArrayList<Double[]> graph = new ArrayList<Double[]>();
	
	
	public equation(double size, double a, double b, double c, double d, double e, double f) {
		
		this_a = a;
		this_b = b;
		this_c = c;
		this_d = d;
		this_e = e;
		this_f = f;
		
		int N = 100;
		Double[] X = new Double[N+1];
		Double[] Y = new Double[N+1];

		X[0] = size;
		Y[0] = size;

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
	
	
	public ArrayList<Double[]> getGraph(){
		return graph;
	}
	

}
