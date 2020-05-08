#include <Python.h>
#include <stdio.h>
#include <string.h>

void print_python_bytes(PyObject *p)
{
	unsigned int i;  
	
	if(PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
		printf("  trying string: %s\n", (PyBytesObject *)p->ob_sval);
		if (((PyVarObject *)p)->ob_size < 10)
			printf("  first %ld bytes:", ((PyVarObject *)p)->ob_size + 1);
		else
			printf("  first 10 bytes:");
		for (i = 0; i <= ((PyVarObject *)p)->ob_size && i < 10; i++)
			printf(" %02hhx", (PyBytesObject *)p->ob_sval[i]);
		printf("\n");
	}
	printf("  [ERROR] Invalid Bytes Object\n");
	return;
}

void print_python_list(PyObject *p)
{
	unsigned int i;

	len = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", (PyListObject *)p->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %ld: %s\n", i, (py_item->ob_item[i])->ob_type->tp_name);
		if (PyBytes_Check(PyList_GET_ITEM(p, i))))
			print_python_bytes(py_item->ob_item[i]);
	}
}
