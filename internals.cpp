#include "headers.h"

VOID get_path() { //fix later
    Py_Initialize();
    FILE* fp = fopen("get_directory.py", "r");
    PyRun_SimpleFile(fp, "get_directory.py");
    fclose(fp);
    Py_Finalize();
    
}