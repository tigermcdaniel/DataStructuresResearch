import matplotlib.pyplot as plt 
import numpy as np 
import csv

# Read in all the data from data files 
with open('LinkedListDataSetA.csv') as csv_file:
    Data = csv.reader(csv_file)
    line_count = 0
    searchLLDataA = []
    insertLLDataA= []
    x_values = []

    for row in csv.reader(csv_file):
        #insert first 
        if(line_count < 400):
            insertLLDataA.append(int(row[0]))
            x_values.append(line_count)

        if(line_count >= 400):
            searchLLDataA.append(int(row[0]))

        line_count = line_count +1
with open('LinkedListDataSetB.csv') as csv_file:
    Data = csv.reader(csv_file)
    line_count = 0
    searchLLDataB = []
    insertLLDataB= []

    for row in csv.reader(csv_file):
        #insert first 
        if(line_count < 400):

            insertLLDataB.append(int(row[0]))
            line_count = line_count + 1

        else:

            searchLLDataB.append(int(row[0]))
with open('BSTDataSetA.csv') as csv_file:
    Data = csv.reader(csv_file)
    line_count = 0
    searchBSTDataA = []
    insertBSTDataA = []

    for row in csv.reader(csv_file):
        #insert first 
        if(line_count < 400):

            insertBSTDataA.append(int(row[0]))
            line_count = line_count + 1

        else:

            searchBSTDataA.append(int(row[0]))
with open('BSTDataSetB.csv') as csv_file:
    Data = csv.reader(csv_file)
    line_count = 0
    searchBSTDataB = []
    insertBSTDataB = []

    for row in csv.reader(csv_file):
        #insert first 
        if(line_count < 400):

            insertBSTDataB.append(int(row[0]))
            line_count = line_count + 1

        else:

            searchBSTDataB.append(int(row[0]))
with open('DataSetASummary.csv') as csv_file:
    Data = csv.reader(csv_file)
    line_count = 0
    dataSetA = []

    for row in csv.reader(csv_file):
        dataSetA.append(int(row[0]))
with open('DataSetBSummary.csv') as csv_file:
    Data = csv.reader(csv_file)
    line_count = 0
    dataSetB = []

    for row in csv.reader(csv_file):
        dataSetB.append(int(row[0]))
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

figC = plt.figure()
figC.subplots_adjust(hspace = 0.4, wspace = 0.4)
figC.suptitle('Search Summary for Set B')
figC.set_size_inches(14, 5, forward=True) 

ax0 = figC.add_subplot(1, 3, 1)
ax0.plot(x_values, searchLLDataB)
ax0.set_title('Linked List Search')
ax0.set_xlabel('Iteration')
ax0.set_ylabel('Time(microseconds)')

ax1 = figC.add_subplot(1, 3, 2)
ax1.plot(x_values, searchBSTDataB)
ax1.set_title('Binary Search Tree Search')
ax1.set_xlabel('Iteration')
ax1.set_ylabel('Time(microseconds)')

ax2 = figC.add_subplot(1, 3, 3)
ax2.plot(x_values, searchHash_LP_DataB)
ax2.set_title('Hash Table: Linear Probing Search')
ax2.set_xlabel('Iteration')
ax2.set_ylabel('Time(microseconds)')

plt.show()