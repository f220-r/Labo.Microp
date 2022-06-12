#include <stdint.h>
#include <repplies.hpp>
using namespace msg_rep;

typedef enum {Greeted, Passed, Identify, Error} states;

class Msg{
    private:
    string message;
    states state;

    public:
    Msg(string _message): message(_message){}
    ~Msg(){}

    void init(){}
    void fsm(){
        switch(state) {
            case Greeted:
                if (message.compare("Hola") == 0){
                    state = Identify;
                    ok();
                }
                else 
                    printf("Message unknown");
                
            break;
            case Identify:
                if(identify(message)){
                    ok();
                    state = Passed;
                }
                else
                    state = Error;
            break;
            case Passed:
                if(passed(message)){
                    ok();
                }
                else
                    state = Error;
            break;
            case Error:
                error();
            break;
        }
    }
};
