#include "Python.h"
#include <limits.h>
 
#define BITS_IN_int     ( sizeof(int) * CHAR_BIT )
#define THREE_QUARTERS  ((int) ((BITS_IN_int * 3) / 4))
#define ONE_EIGHTH      ((int) (BITS_IN_int / 8))
#define HIGH_BITS       ( ~((unsigned int)(~0) >> ONE_EIGHTH ))
 
/*
    PJW hashing algorythm
*/
static PyObject* mythhash_hashPJW(PyObject *self, PyObject *args) {

    const unsigned char *name;
    unsigned int hash_value, i;
    
    if (!PyArg_ParseTuple(args, "s", &name))
        return NULL;
     
    for ( hash_value = 0; *name; ++name ) {
        hash_value = ( hash_value << ONE_EIGHTH ) + *name;
        if (( i = hash_value & HIGH_BITS ) != 0 )
            hash_value = ( hash_value ^ ( i >> THREE_QUARTERS )) & ~HIGH_BITS;
    }
    return Py_BuildValue("i", hash_value);
}


/*
    ELF hashing algorythm
*/
static PyObject* mythhash_hashELF(PyObject *self, PyObject *args) {

    const unsigned char *name;
    unsigned long h = 0, g;

    if (!PyArg_ParseTuple(args, "s", &name))
        return NULL;

    while ( *name )
    {
        h = ( h << 4 ) + *name++;
        if ( g = h & 0xF0000000 ) 
            h ^= g >> 24;
        h &= ~g;
    }
    return Py_BuildValue("i", h);
}

/*
 * Our method declararations
 */
static PyMethodDef kMythhashMethods[] = {
  {"hashELF", mythhash_hashELF, METH_VARARGS,
   "ELF hashing algorythm. Takes string and return int"},
  {"hashPJW", mythhash_hashPJW, METH_VARARGS,
   "PJW hashing algorythm. Takes string and return int"},
  {NULL, NULL, 0, NULL}
};
/*
 * Module initialization
 */
PyMODINIT_FUNC inithashes(void) {
    Py_InitModule("hashes", kMythhashMethods);
}
