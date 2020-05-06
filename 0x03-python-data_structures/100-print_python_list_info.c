#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *hold;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		hold = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, hold->ob_type->tp_name);
	}
}