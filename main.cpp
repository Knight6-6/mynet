#include "core/server.hpp"
#include "logger.hpp"

int main()
{
    logger::getlogger().error(999, "FORCE LOG START");
    server Server;
    if(Server.init("127.0.0.1" , 5050))
    {
        Server.start();
    }
    
    return 0;
}