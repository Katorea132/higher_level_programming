#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
	unsigned int i, valp = 0;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
		printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
		if (((PyVarObject *)p)->ob_size >= 10)
			valp = 10;
		else
			valp += (((PyVarObject *)p)->ob_size + 1;
		printf("  first %d bytes: ", valp);
		for (i = 0; i < valp; i++)
		{
			printf("%02hhx", ((PyBytesObject *)p)->ob_sval[i]);
			if (i + 1 < valp)
				printf(" ");
		}
		printf("\n");
	}
	printf("  [ERROR] Invalid Bytes Object\n");
	return;
}

void print_python_list(PyObject *p)
{
	PyObject *item;
	unsigned int i;

	if (PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", ((PyVarObject *)p)->ob_size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < ((PyVarObject *)p)->ob_size; i++)
		{
			item = PySequence_GetItem(p, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
		}
	}
}
