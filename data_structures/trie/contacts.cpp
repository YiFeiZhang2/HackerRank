#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

class node{
private:
    char m_cont;
    //vector <node*> m_children;
    int m_matches;
public:
    node* m_children[26] = { };
    node ();
    ~node ();
    char get_cont();
    void set_cont(char c);
    node* find_child(char c);
    void add_child(node* child);
    int get_matches();
    void add_match();
};

class trie{
private:
    //node* root;
public:
    node* root;
    trie();
    ~trie();
    void add_string(string s);
    int search_partial(string s);
};

node::node () : m_cont(' '), m_matches(0) { }

node::~node () {}

char node::get_cont() { return m_cont; }

void node::set_cont(char c) { m_cont = c; }

node* node::find_child(char c) {
    int ind = int(c) - 97;              //converts the ascii value of the character into
                                        //0 - 25 index of the m_children vector
    if (m_children[ind] != NULL)
        return m_children[ind];
    return NULL;
}

void node::add_child(node* child) {
    int ind = int(child->get_cont()) - 97;
    m_children[ind] = child;
}

int node::get_matches() { return m_matches; }

void node::add_match() { m_matches += 1; }

trie::trie () : root(new node()) { }

trie::~trie() { }

void trie::add_string(string s) {
    node* current = root;
    
    for (unsigned int i = 0; i < s.length(); i++){
        node* child = current->find_child(s[i]);
        if (child != NULL) {
            child->add_match();
            current = child;
        }            
        else {
            node* temp = new node();
            temp->set_cont(s[i]);
            temp->add_match();
            current->add_child(temp);
            current = temp;
        }
    }
}

int trie::search_partial(string s) {
    node* current = root;
    

    for (unsigned int i = 0; i < s.length(); i++){
        node* temp = current->find_child(s[i]);
        
        if (temp == NULL)
            return 0;
        else{
            current = temp;
        }
    }
    
    return current->get_matches();
}

int main(){
    int n;
    string cmd;
    string word;
    trie* t = new trie();

    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> cmd;
        cin >> word;
        if (cmd == "add")
            t->add_string(word);
        else
            cout << t->search_partial(word) << endl;
    } 
}