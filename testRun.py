import matplotlib.pyplot as plt 
import numpy as np 
import csv

# Read in all the data from data files 
with open('HashTable_LinearProbing_DataSetA.csv') as csv_file:
    Data = csv.reader(csv_file)
    line_count = 0
    searchHash_LP_DataA = []
    insertHash_LP_DataA = []
    x_values = []

    for row in csv.reader(csv_file):
        #insert first 
        if(line_count < 400):

            x_values.append(line_count)
            insertHash_LP_DataA.append(int(row[0]))

        if(line_count >= 400):
            searchHash_LP_DataA.append(int(row[0]))

        line_count = line_count +1
with open('HashTable_LinearProbing_DataSetB.csv') as csv_file:
    Data = csv.reader(csv_file)
    line_count = 0
    searchHash_LP_DataB = []
    insertHash_LP_DataB = []

    for row in csv.reader(csv_file):
        #insert first 
        if(line_count < 400):

            insertHash_LP_DataB.append(int(row[0]))

        if(line_count >= 400):
            searchHash_LP_DataB.append(int(row[0]))

        line_count = line_count + 1
with open('HashTable_QuadraticProbing_DataSetB.csv') as csv_file:
    Data = csv.reader(csv_file)
    line_count = 0
    searchHash_QP_DataB = []
    insertHash_QP_DataB = []

    for row in csv.reader(csv_file):
        #insert first 
        if(line_count < 400):

            insertHash_QP_DataB.append(int(row[0]))

        if(line_count >= 400):
            searchHash_QP_DataB.append(int(row[0]))

        line_count = line_count + 1
with open('HashTable_QuadraticProbing_DataSetA.csv') as csv_file:
    Data = csv.reader(csv_file)
    line_count = 0
    searchHash_QP_DataA = []
    insertHash_QP_DataA = []

    for row in csv.reader(csv_file):
        #insert first 
        if(line_count < 400):

            insertHash_QP_DataA.append(int(row[0]))
        if(line_count >= 400):

            searchHash_QP_DataA.append(int(row[0]))

        line_count = line_count + 1
with open('HashTable_Chaining_DataSetB.csv') as csv_file:
    Data = csv.reader(csv_file)
    line_count = 0
    searchHash_C_DataB = []
    insertHash_C_DataB = []

    for row in csv.reader(csv_file):
        #insert first 
        if(line_count < 400):

            insertHash_C_DataB.append(int(row[0]))

        if(line_count >= 400):

            searchHash_C_DataB.append(int(row[0]))
        line_count = line_count + 1
with open('HashTable_Chaining_DataSetA.csv') as csv_file:
    Data = csv.reader(csv_file)
    line_count = 0
    searchHash_C_DataA = []
    insertHash_C_DataA = []

    for row in csv.reader(csv_file):
        #insert first 
        if(line_count < 400):

            insertHash_C_DataA.append(int(row[0]))

        if(line_count >= 400):

            searchHash_C_DataA.append(int(row[0]))
        line_count = line_count + 1


plt.plot(x_values, insertBSTDataB, color = 'red', label = 'Avg Insertion Time')
plt.plot(x_values, searchBSTDataB, color = 'green', label = 'Avg Search Time')
plt.legend(loc = 'upper left')
plt.title('Data B: Binary Search Tree')
plt.xlabel('Iterations')
plt.ylabel('Time(microseconds)')
plt.show()

# Hash Table: Data A
figC = plt.figure()
figC.subplots_adjust(hspace = 0.4, wspace = 0.4)
figC.suptitle('Hash Table Results for Set A')
figC.set_size_inches(12, 7, forward=True) 

# Hash Table: Linear Probing 
ax0 = figC.add_subplot(2, 3, 1)
ax0.plot(x_values, insertHash_LP_DataA, color = 'green')
ax0.set_title('Linear Probing: Avg Insertion Time')
ax0.set_xlabel('Iteration')
ax0.set_ylabel('Time(microseconds)')

ax1 = figC.add_subplot(2, 3, 4)
ax1.plot(x_values, searchHash_LP_DataA, color = 'red')
ax1.set_title('Linear Probing: Avg Search Time')
ax1.set_xlabel('Iteration')
ax1.set_ylabel('Time(microseconds)')

# Hash Table: Quadratic Probing 
ax2 = figC.add_subplot(2, 3, 2)
ax2.plot(x_values, insertHash_QP_DataA, color = 'green')
ax2.set_title('Quadratic Probing: Avg Insertion Time')
ax2.set_xlabel('Iteration')
ax2.set_ylabel('Time(microseconds)')

ax3 = figC.add_subplot(2, 3, 5)
ax3.plot(x_values, searchHash_QP_DataA, color = 'red')
ax3.set_title('Quadratic Probing: Avg Search Time')
ax3.set_xlabel('Iteration')
ax3.set_ylabel('Time(microseconds)')

# Hash Table: Chaining
ax4 = figC.add_subplot(2, 3, 3)
ax4.plot(x_values, insertHash_C_DataA, color = 'green')
ax4.set_title('Chaining: Avg Insertion Time')
ax4.set_xlabel('Iteration')
ax4.set_ylabel('Time(microseconds)')

ax5 = figC.add_subplot(2, 3, 6)
ax5.plot(x_values, searchHash_C_DataA, color = 'red')
ax5.set_title('Chaining: Avg Search Time')
ax5.set_xlabel('Iteration')
ax5.set_ylabel('Time(microseconds)')

plt.show()

# Hash Table: Data B
figD = plt.figure()
figD.subplots_adjust(hspace = 0.4, wspace = 0.4)
figD.suptitle('Hash Table Results for Set B')
figD.set_size_inches(12, 7, forward=True) 

# Hash Table: Linear Probing 
ax0 = figD.add_subplot(2, 3, 1)
ax0.plot(x_values, insertHash_LP_DataB, color = 'green')
ax0.set_title('Linear Probing: Avg Insertion Time')
ax0.set_xlabel('Iteration')
ax0.set_ylabel('Time(microseconds)')

ax1 = figD.add_subplot(2, 3, 4)
ax1.plot(x_values, searchHash_LP_DataB, color = 'red')
ax1.set_title('Linear Probing: Avg Search Time')
ax1.set_xlabel('Iteration')
ax1.set_ylabel('Time(microseconds)')

# Hash Table: Quadratic Probing 
ax2 = figD.add_subplot(2, 3, 2)
ax2.plot(x_values, insertHash_QP_DataB, color = 'green')
ax2.set_title('Quadratic Probing: Avg Insertion Time')
ax2.set_xlabel('Iteration')
ax2.set_ylabel('Time(microseconds)')

ax3 = figD.add_subplot(2, 3, 5)
ax3.plot(x_values, searchHash_QP_DataB, color = 'red')
ax3.set_title('Quadratic Probing: Avg Search Time')
ax3.set_xlabel('Iteration')
ax3.set_ylabel('Time(microseconds)')

# Hash Table: Chaining
ax4 = figD.add_subplot(2, 3, 3)
ax4.plot(x_values, insertHash_C_DataB, color = 'green')
ax4.set_title('Chaining: Avg Insertion Time')
ax4.set_xlabel('Iteration')
ax4.set_ylabel('Time(microseconds)')

ax5 = figD.add_subplot(2, 3, 6)
ax5.plot(x_values, searchHash_C_DataB, color = 'red')
ax5.set_title('Chaining: Avg Search Time')
ax5.set_xlabel('Iteration')
ax5.set_ylabel('Time(microseconds)')

plt.show()