#include<iostream>
using namespace std;
class employee{
    char name[50];
    float salary;
    public:
    void get();
    void display();
};
void employee:: get(){
    cout<<"Name of the Employee : "<<endl;
    cin>>name;
    cout<<"Salary of the Employee : "<<endl;
    cin>>salary;
}
void employee:: display(){
    cout<<"Name = "<<name<<endl;
    cout<<"Salary = "<<salary<<endl;

}

class manager : public employee{
    char dept[30];
    public:
    void get();
    void tostring();
};
void manager:: get(){
    employee::get();
    cout<<"Department of the employee : "<<endl;
    cin>>dept;
}
void manager:: tostring(){
    employee::display();
    cout<<"Department : "<<dept<<endl;
}
class executive: public manager{
    public:
    void tostring(){
        cout<<"Executive : "<<endl;
        manager::tostring();
    }

};

int main(){
    executive emp;
    emp.get();
    emp.tostring();

    return 0;
}
