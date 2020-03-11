package posterity;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

import org.apache.commons.math3.stat.regression.SimpleRegression;

import Jama.Matrix;

public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		double time = 0.0;
		double flux_people = 20.0;
		double num_people = 100.0;
		double pace = 0.1667; //Minutes of average song divided by 240.0
		double heat = 0.83; // Subj probability from 0 to 1 that there will be dancing
		int intervals = (int) (4.0/pace); //Number of songs in 4 hours
		double heatdelta = 1.0/(4.0/pace); // For incrementing the heat variable at the end of each song
		int size = 3; // Groups of 6, 14, and 24 will fight it out to end up bison or cattle
		double wisdom = 0.12; // This is gaussian for both sides but a necessary variable in the lanchester
		
		//System.out.println(intervals);
		//System.out.println(heatdelta);
		
		
		// This is the size of group that should be approached
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
		
		// increment force and cohesion for later battles
		double forcedelta = (size/3)/intervals;
		double cohdelta = (size/6)/intervals;
		double cohb = cohdelta; //cohesion at most one sixth of size
		double cohc = cohdelta;
		double forceb = forcedelta; // at most one third of size
		double forcec = forcedelta; //at most one third of size
		
		double[] raw_heats = new double[(int)num_people -2];
		// Raw heats at the beginning
		raw_heats = ehrenfest.chain(num_people, heat);
		double max_raw = 0.000001;
		for(int i = 0; i < (int)num_people - 2; i++) {
			if(max_raw > raw_heats[i]) {
				max_raw = raw_heats[i];
			}
		}
		double raw_heats_score = raw_heats[(int)(heat*size)]/max_raw;
		lanchester raw_battle = new lanchester(num_people,intervals,cohb,wisdom,forceb,wisdom,cohc,forcec);
		
		
		dance equilibrium = new dance(0.5, heatdelta, size, raw_heats_score);
		dance actual = new dance(heat, heatdelta, size, raw_heats_score);
		
		double[][] eqreg = new double[equilibrium.heatcount][2];
		for(int i = 0; i < equilibrium.heatcount; i++) {
			eqreg[i][0] = i;
			eqreg[i][1] = equilibrium.bdchain[i];
			//System.out.println(equilibrium.bdchain[i]);
		}
		
		double[][] actualreg = new double[actual.heatcount][2];
		for(int i = 0; i < actual.heatcount; i++) {
			actualreg[i][0] = i;
			actualreg[i][1] = actual.bdchain[i];
			//System.out.println(actual.bdchain[i]);
		}
		
		
		SimpleRegression eqobj = new SimpleRegression();
		SimpleRegression actualobj = new SimpleRegression();
		eqobj.addData(eqreg);
		actualobj.addData(actualreg);
		double eqslope = eqobj.getSlope();
		double actualslope = actualobj.getSlope();
		
		
		cohc = (actualslope/eqslope)*(size/6);
		System.out.println(cohc);
		Set<double[][]> graphs = raw_battle.getGraphs(cohc, actual.heatcount, actual.bdchain, size, flux_people, cohdelta, forcedelta);
		
		
		for(double[][] graph : graphs) {
			
			double[][] bison = new double[100][2];
			double[][] cattle = new double[100][2];
			
			boolean death1 = false;
			boolean death2 = false;
			
			for(int i=0; i < 100; i++) {
				bison[i][0] = i;
				cattle[i][0] = i;
				bison[i][1] = graph[i][0];
				cattle[i][1] = graph[i][1];
				
				if(graph[i][0] < 0 || graph[i][1] < 0) {
					death1 = true;
				}
				if(graph[i][0] < 0 && graph[i][1] < 0) {
					death2 = true;
				}
				
				
				
			}
			
			if(death1 == false && death2 == false) {
				for(int i=0; i < 100; i++) {
					System.out.println(i + "," + bison[i][1] + "," + cattle[i][1]);
				}
			}
			
		}
		
		
		//double[][] bdchain = new double[intervals][intervals];
		
		// Number of Steps likely to end up with all cattle or all bison
		
		
		
		//System.out.println(raw_heats);
		
		// System of Lanchester 2. Returns values for Bison[.get(0)], Cattle[.get(1)]
		
		
		//ArrayList<Double[]> graph = raw_battle.getGraph();
		
		
		//for(int i = 0; i <= intervals; i++) {
			
			//System.out.println(graph.get(0)[i]);
			//System.out.println(graph.get(1)[i]);
			
		//}
		
		

	}

}
