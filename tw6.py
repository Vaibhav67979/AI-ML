import csv
a = []

with open('enjoysport.csv','r') as csvfile:
    next(csvfile)
    for row in csv.reader(csvfile):
        a.append(row)
    print(a)

print("\nThe total number of training instances : ", len(a))

num_attribute = len(a[0])-1

print("The initial hypothesis is : ")
hypothesis = ['0']*num_attribute
print(hypothesis)

for i in range(0, len(a)):
    if a[i][num_attribute] == 'yes':
        print(f"\nInstance {i+1} is {a[i]} and is positive instance")
        for j in range(0, num_attribute):
            if hypothesis[j] == '0' or hypothesis[j] == a[i][j]:
                hypothesis[j] = a[i][j]
            else:
                hypothesis[j] = '?'
        print(f"The hypothesis for the training instance {i+1} is {hypothesis} \n")

    if a[i][num_attribute] == 'no':
        print(f"The instance {i+1} is {a[i]} and is negative instance and hence is ignored.")
        print(f"The hypothesis for the negative training instance {i+1} is {hypothesis} \n")

print(f"\nThe maximally specific hypothesis for the training instance is {hypothesis}")