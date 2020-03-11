package posterity;

import java.util.ArrayList;

public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		
		double num_people = 12.0;
		double flux_people = 3.0;
		double dance = 0.8;
		double pace = 0.34;
		int intervals = (int) Math.round(4.0/pace);
		
		int size = 3;
		
		if(num_people/3 <= 5) {
			size = 3;
		}else if(num_people/7 <= 5) {
			size = 7;
		}else {
			size = 12;
		}
		
		
		
		
		double[][] bdchain = new double[intervals][intervals];
		
		// Number of Steps likely to end up with all cattle or all bison
		double raw_dances = ehrenfest.chain(num_people, dance);
		
		
		System.out.println(raw_dances);
		
		
		equation eq = new equation(num_people,num_people,1.61,0.12,3.0,0.12,1.75,3.5);
		
		ArrayList<Double[]> graph = eq.getGraph();
		
		
		for(int i = 0; i <= 100; i++) {
			
			//System.out.println(graph.get(0)[i]);
			System.out.println(graph.get(1)[i]);
			
		}
		
		

	}

}
