#include <stdint.h>
#include <led.hpp>

class blink

{

public:


explicit blink (int l, int32_t &count): _led(l), _count(_count){}
~blink();
void FSM(){

switch (_state)
case on:
if(_count<0){

off();
_state=off; 
_count= t_off;

}


case off:
if(_count<0){
    on();
_state=on; 
_count= t_on;
}
}
void init()
{
    led::init(l);
    on();
}


private:

uint8_t led; // nro de led
uint32_t &count; //recibe por referencia un contador 

enum class _state{

void on(){
    led::on(_led);    }
void off(){
led::off(_led);}
};


static constexpr uint32_t t_on= 300;
static constexpr uint32_t t_off= 300;

};