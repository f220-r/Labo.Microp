#include <stdint.h>
#include <button.hpp>

using namespace button;

typedef enum {Released, Hold_HL, Pressed, Hold_LH} states;

class Debounce{
    private:
    uint8_t button_var;
    uint32_t button_count = 0;
    states state;
    public:
    Debounce(uint8_t _button, uint32_t _button_count) : button_var(_button),button_count(_button_count){}
    ~Debounce() {}

    void init() { 
        state = Released;
        released();
    }
    void fsm(){
        switch(state){
            case Released:
                if(button_var == 1){
                    hold_HL();
                    state = Hold_HL;
                    button_count = 0;
                }
            break;
            case Hold_HL:
                if(button_count == 50){
                    pressed();
                    state = Pressed;
                }
            break;
            case Hold_LH:
                if(button_count == 50){
                    released();
                    state = Released;
                }
            break;
            case Pressed:
                if(button_var == 0){
                    hold_LH();
                    state= Hold_LH;
                    button_count = 0;
                }
            break;
        }
        button_count++;
    }
};
