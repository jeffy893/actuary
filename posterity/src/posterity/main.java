package posterity;

import java.util.ArrayList;

import Jama.Matrix;

public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		double time = 0.0;
		double flux_people = 3.0;
		double num_people = 100.0;
		double pace = 0.0208333;
		double dance = 0.49;
		int intervals = (int) Math.round(4.0/pace);
		double dancedelta = 1/intervals;
		
		int size = 3;
		double wisdom = 0.12;
		
		if(num_people/3 <= 5) {
			size = 3;
			wisdom = 0.03;
		}else if(num_people/7 <= 5) {
			size = 7;
			wisdom = 0.07;
		}else {
			size = 12;
			wisdom = 0.12;
		}
		
		double forcedelta = (size/3)/intervals;
		double cohdelta = (size/6)/intervals;
		
		double cohb = cohdelta; //cohesion at most one sixth of size
		double cohc = cohdelta;
		double forceb = forcedelta; // at most one third of size
		double forcec = forcedelta; //at most one third of size
		
		
		// Most raw ehrenfest steps
		double raw_comb = ehrenfest.chain(num_people,0.5);
		// Raw Dances at the beginning
		double raw_dances = ehrenfest.chain(num_people, dance);
		double raw_dances_score = raw_dances/raw_comb;
		//initial battle
		lanchester raw_battle = new lanchester(size,intervals,cohb,wisdom,forceb,wisdom,cohc,forcec);
		
		
		//At each pace, a battle takes place. This informs a birth and death chain
		
		double[] bdcomeup = new double[intervals];
		double[] bdlongevity = new double[intervals];
		
		double comeup = 0.5 - dancedelta;
		double comeupdances = 1.0;
		double comeupscore = 1.0;
		
		for(int i = 0; i < intervals; i++) {
			
			
			comeupdances = ehrenfest.chain(size, comeup);
			comeupscore = comeupdances/raw_comb;
			bdcomeup[i] = comeupscore;
			
			comeup = comeup - dancedelta;
		}
		
		double longevity = 0.5 + dancedelta;
		double longevitydances = 1.0;
		double longevityscore = 1.0;
		
		for(int i = 0; i < intervals; i++) {
			
			longevitydances = ehrenfest.chain(size, longevity);
			longevityscore = longevitydances/raw_comb;
			bdlongevity[i] = longevityscore;
			
			
			longevity = longevity + dancedelta;
		}
		
		
		
		Matrix bdchain = birthdeath.chain(bdcomeup, bdlongevity, raw_dances_score, intervals);
		
		
		
		
		
		
		
		//double[][] bdchain = new double[intervals][intervals];
		
		// Number of Steps likely to end up with all cattle or all bison
		
		
		
		//System.out.println(raw_dances);
		
		// System of Lanchester 2. Returns values for Bison[.get(0)], Cattle[.get(1)]
		
		
		//ArrayList<Double[]> graph = raw_battle.getGraph();
		
		
		//for(int i = 0; i <= intervals; i++) {
			
			//System.out.println(graph.get(0)[i]);
			//System.out.println(graph.get(1)[i]);
			
		//}
		
		

	}

}
