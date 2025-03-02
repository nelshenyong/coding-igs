public class Soal3
{
private int[] testArray = {3, 4, 5};
/** @param n an int to be incremented by 1 */
public void increment (int n)
{ n++; }
public void firstTestMethod()
{
for (int i = 0; i < testArray.length; i++)
{
increment(testArray[i]);
System.out.print(testArray[i] + " ");
}
}
public void secondTestMethod()
{
for (int element : testArray)
{
increment(element);
System.out.print(element + " ");
}
}
}