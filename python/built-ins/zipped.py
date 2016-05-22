numCla, numStu = map(int, input().strip().split(" "))
class_ave = list()
for i in range(numStu):
    class_ave.append(list(map(float, input().strip().split(" "))))
stud_mark = list(zip(*class_ave))
#for i in range(len(stud_mark)):
#    print(sum(stud_mark[i])/numStu) 
class_mark = [sum(i)/numStu for i in stud_mark]
print('\n'.join(map(str, class_mark)))
