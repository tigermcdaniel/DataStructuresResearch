#include "hash.hpp"
#include <string>
#include <iostream>

using namespace std;
//table size: m = 40,009
//hash function: h(x) = x % m;

HashTable::HashTable(int bsize) {
    tableSize = bsize;

    //initialize the array of nodes and point the head to the start of them 
    head = new NODE[bsize];
    numOfcolision = 0;
}

/*
* resolution 1 will be linear addressing
* ie look for next available position with the next highest index
*/
bool HashTable::resolution1(int key, int hashIndex) {
    //resolution 1: linear probing     
    //start from 0 until the end 
    for (int i = 0; i < tableSize; i++)
    {
        if (head[i].initialized == false)
        {
            head[i].key = key;
            head[i].initialized = true;
            return true;
        }
    }
    return false;
}

/*
* resolution 2 will recursively perform quadratic probing to try and find a spot
*/
bool HashTable::resolution2(int key, int startingIndex, int index) {
    if (startingIndex == index) return false;

    int newHash = startingIndex + (index * index);
    while (newHash >= tableSize) {
        newHash = newHash - tableSize;
    }
    NODE* current = &head[newHash];
    if (current != nullptr && current->initialized == false) {
        current->key = key;
        current->initialized = true;
        return true;
    }
    else {
        resolution2(key, startingIndex, index + 1);
    }
}

/*
* resolution 3 will perform linked list chainging to add the element
*/
bool HashTable::resolution3(int key, NODE* current) {
    NODE* insert = new NODE();
    insert->key = key;
    insert->initialized = true;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = insert;
    return true;
}

bool HashTable::insertItem(int key, int collisonRes) {
    NODE* insert = new NODE();
    insert->key = key;

    //index is the position is will ideally be stored under 
    int index = key % tableSize;
    NODE* current = &head[index];
    bool added = false;

    if (current->initialized == false) {
        head[index].key = key;
        head[index].initialized = true;
        added = true;
    }
    else {
        //we have a collision
        if(collisonRes == 1){
            return(resolution1(key, index));
        }

        if (collisonRes == 2) {
           return(resolution2(key, index, 0));
        }

        return (resolution3(key, current));
    }
    return added;
}

int HashTable::getNumOfCollision() {
    return numOfcolision;
}

NODE* HashTable::searchItem(int key) {
    for (int i = 0; i < tableSize; i++)
    {
        NODE* current = &head[i];

        if (current != NULL && current->initialized == true)
        {
            if (current->key == key) {
                return current;
            }

            if (current->next != NULL && current->next->initialized == true)
            {
                NODE* index = current->next;
                while (index != NULL && index->initialized == true)
                {
                    if (index->key == key) {
                        return index;
                    }
                    index = index->next;
                }
            }
        }
    }
    return NULL;
}

void HashTable::printTable() {
    for (int i = 0; i < 40000; i++) {
        if ((head + i) == NULL) {
            cout << "NULL -> " << endl;
        }
        else {
            cout << (head + i)->key << " -> " << endl;
        }
    }
}