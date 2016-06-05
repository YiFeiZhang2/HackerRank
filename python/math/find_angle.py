# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(raw_input())
BC = int(raw_input())
print(str(int(round(math.degrees(math.atan2(AB,BC))))) + '°')
