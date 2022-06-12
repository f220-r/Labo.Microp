#include <stdio.h>
#include <string>
using std::string;

namespace msg_rep{
    void hello();
    void ok();
    void error();
    bool identify(string message);
    bool passed(string message);
}