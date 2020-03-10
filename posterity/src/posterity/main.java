package posterity;

public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		
		int num_people = 100;
		double flux_people = 3.0;
		double dance = 0.8;
		double pace = 4.0;
		int intervals = (int) Math.round(240.0/pace);
		
		
		
		
		double[][] bdchain = new double[intervals][intervals];
		
		// Number of Steps likely to end up with all cattle or all bison
		double raw_dances = ehrenfest.chain(num_people, dance);
		
		
		System.out.println(raw_dances);
		
		
		
		
		

	}

}
