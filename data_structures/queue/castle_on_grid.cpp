//Castle on Grid Challenge, and practice with classes
//and queues in cpp

#include <iostream>
using namespace std;

class Node {
private:
    Node* next = NULL;
public:
    int x;
    int y;
    Node (int x, int y) : x (x), y (y), next (NULL) { };
    Node () { };
    Node* getNext(){
        return this->next;
    }
    void setNext(Node* n){
        this->next = n;
    }
    int* getVal(){
        static int p[2];
        p[0] = this->x;
        p[1] = this->y;
        return p;
    }
};

class Queue {
private:
    Node* head = NULL;
    Node* tail = NULL;
public:
    Queue (int x, int y);
    void push(int x, int y);
    Node pop();
    bool isEmpty();
    void print();
};

Queue::Queue (int x, int y){
    Node* n = new Node(x, y);
    this->head = n;
    this->tail = n;
}

void Queue::push(int x, int y){
    Node* n = new Node(x, y);
    if (this->head != NULL){
        this->tail->setNext(n);
        this->tail = n;
    } else {
        this->head = n;
        this->tail = n;
    }
}

Node Queue::pop(){
    Node* x = this->head;
    this->head = x->getNext();
    return *x;
}

bool Queue::isEmpty(){
    return (this->head == NULL);
}

void Queue::print(){
    int* p;
    Node* x = this->head;
    while (x != NULL){
        p = x->getVal();
        cout << p[0] << " " << p[1] << endl;
        x = x->getNext();
    }
}


template <typename T>
void print_2d_arr(T(arr)[], int size){
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++)
            cout << arr[i][j] << " ";
        cout << endl;
    }
}

int main () {
    int startPos[2];
    int endPos[2];
    int size;
    cin >> size;
    char c;
    bool* roadMap[size];
    int* seenMap[size];
    for (int i = 0; i < size; i++){
      roadMap[i] = new bool[size];
      seenMap[i] = new int[size];
    }   

    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++){
            cin >> c;
            if (c == '.') {
                roadMap[i][j] = true;
            } else {
                roadMap[i][j] = false;
            }
            seenMap[i][j] = -1;
        }
    }
    
    cin >> startPos[0] >> startPos[1] >> endPos[0] >> endPos[1];
    //print_2d_arr(roadMap, size);
    seenMap[startPos[0]][startPos[1]] = 0;
    //print_2d_arr(seenMap, size);
    
    Queue q (startPos[0], startPos[1]);
    int* coord;
    Node n;
    while (!q.isEmpty()){
        //cout << "curr queue" << endl;
        //q.print();
        n = q.pop();
        coord = n.getVal();
        if (coord[0] == endPos[0] && coord[1] == endPos[1]){
            cout << seenMap[coord[0]][coord[1]] << endl;
            return 0;
        }
        bool goUp = true;
        bool goDown = true;
        bool goLeft = true;
        bool goRight = true;
        int dist = 1;
        while (goUp || goDown || goLeft || goRight) {
            if (coord[1] - dist < 0 || roadMap[coord[0]][coord[1] - dist] == false)
                goUp = false;
            if (coord[1] + dist >= size || roadMap[coord[0]][coord[1] + dist] == false)
                goDown = false;
            if (coord[0] - dist < 0 || roadMap[coord[0] - dist][coord[1]] == false)
                goLeft = false;
            if (coord[0] + dist >= size || roadMap[coord[0] + dist][coord[1]] == false)
                goRight = false;
            
            if (goUp && seenMap[coord[0]][coord[1] - dist] == -1){
                seenMap[coord[0]][coord[1] - dist] = seenMap[coord[0]][coord[1]] + 1;
                q.push(coord[0], coord[1] - dist);
            }
            if (goDown && seenMap[coord[0]][coord[1] + dist] == -1){
                seenMap[coord[0]][coord[1] + dist] = seenMap[coord[0]][coord[1]] + 1;
                q.push(coord[0], coord[1] + dist);
            }
            if (goLeft && seenMap[coord[0] - dist][coord[1]] == -1){
                seenMap[coord[0] - dist][coord[1]] = seenMap[coord[0]][coord[1]] + 1;
                q.push(coord[0] - dist, coord[1]);
            }
            if (goRight && seenMap[coord[0] + dist][coord[1]] == -1){
                seenMap[coord[0] + dist][coord[1]] = seenMap[coord[0]][coord[1]] + 1;
                q.push(coord[0] + dist, coord[1]);
            }
            dist += 1;
        }
    }
    return 0;
}

