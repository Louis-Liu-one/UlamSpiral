
#include <stdlib.h>
#include <stdbool.h>
#include <Python.h>

int size, num;
bool *isprime;

static PyObject *Py_EratothenesBegin(PyObject *self, PyObject *args)
{
    if (!PyArg_ParseTuple(args, "i", &size)) return NULL;
    num = 0;
    if (!(isprime = malloc(size * sizeof(bool)))) return NULL;
    for (int i = 0; i < size; ++i) isprime[i] = true;
    isprime[0] = false;
    Py_RETURN_NONE;
}

static PyObject *Py_EratothenesNext(PyObject *self, PyObject *args)
{
    if (++num > size) Py_RETURN_NONE;
    if (isprime[num - 1])
        for (int comp = num * 2; comp <= size; comp += num)
            isprime[comp - 1] = false;
    return Py_BuildValue("(ii)", num, isprime[num - 1]);
}

static PyObject *Py_EratothenesEnd(PyObject *self, PyObject *args)
{
    free(isprime);
    Py_RETURN_NONE;
}

static PyMethodDef EratothenesMethods[] = {
    {"eratothenes_begin", Py_EratothenesBegin,
        METH_VARARGS, "Begin the sieve of Eratothenes."},
    {"eratothenes_next", Py_EratothenesNext,
        METH_NOARGS,
        "Return the next number and a bool "
        "that means whether it is a prime. Begin with 1."},
    {"eratothenes_end", Py_EratothenesEnd,
        METH_NOARGS, "Do the cleaning."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef EratothenesModule = {
    PyModuleDef_HEAD_INIT, "eratothenes",
    NULL, -1, EratothenesMethods
};

PyMODINIT_FUNC PyInit_eratothenes()
{
    return PyModule_Create(&EratothenesModule);
}
