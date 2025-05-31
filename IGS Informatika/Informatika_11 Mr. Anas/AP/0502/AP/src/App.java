import java.util.*;

public class App {
    private int minSteps;
    private ArrayList<Integer> steps = new ArrayList<Integer>();

    public StepTracker(int ms) {
        minSteps = ms;
    }

    public int activateDays() {
        int counter = 0;
        if(steps.size() == 0){
            return counter;
        }
        for (int step : steps) {
            if (step >= minSteps) {
                counter++;
            }
        }

        return counter;
    }

    public double avarageSteps()
    {
        double sum = 0;
        if(steps.size() == 0){
            return sum;
        }
        for(int step:steps){
            sum+=step;
        }

        return sum/ steps.size();
    }

    public static void main(String[] args) {
        StepTracker tr = new StepTracker(1000);
        System.out.println(tr.activateDays()); //0
        System.out.println(tr.avarageSteps()); //0.0
        tr.addDailySteps(9000)
        
    }
}