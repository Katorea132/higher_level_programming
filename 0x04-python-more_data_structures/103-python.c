#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
	unsigned int valp, i;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
		printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
		if (((PyVarObject *)p)->ob_size >= 10)
			valp = 10;
		else
			valp = ((PyVarObject *)p)->ob_size + 1;
		printf("  first %d bytes: ", valp);
		for (i = 0; i < valp; i++)
		{
			printf("%02hhx", ((PyBytesObject *)p)->ob_sval[i])
			if (i + 1 == valp)
				printf("\n");
			else
				printf(" ");
			
		}
	}
}

void print_python_list(PyObject  *p)
{
	unsigned int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n" PyList_GET_SIZE(p));
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_GET_SIZE(p); i++)
	{
		printf("Element %d: %s\n", i, PySequence_GetItem(p, i)->ob_type->tp_name);
		if (PyBytes_Check(PyList_GET_ITEM(p, i)))
			print_python_bytes(PyList_GET_ITEM(p, i));
	}
}
