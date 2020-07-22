#pragma once
#ifndef HASH_HPP
#define HASH_HPP

#include <string>

using namespace std;

struct NODE
{
    int key;
    struct NODE* next = nullptr;
    bool initialized = false;
};

class HashTable
{
    // No. of buckets (linked lists)
    int tableSize = 0;

    // Pointer to an array containing buckets
    NODE* head = nullptr;

    //store num of collisions 
    int numOfcolision = 0;

    NODE* createNode(int key, NODE* next);

public:

    // Constructor
    HashTable(int bsize);

    // inserts a key into hash table
    bool insertItem(int key,  int collisonRes);

    //linear probing 
    bool resolution1(int key, int hashIndex);

    //quadratic probing 
    bool resolution2(int key, int startingIndex, int index);

    //chaining with linked lists 
    bool resolution3(int key, NODE* current);

    // hash function to map values to key
    unsigned int hashFunction(int key);

    //print the current table sores 
    void printTable();

    //return the num of collisions 
    int getNumOfCollision();

    //return pointer to said node containing key 
    NODE* searchItem(int key);
};

#endif
