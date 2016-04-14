from DynamicModuleLoader import DynamicModuleLoader

dml = DynamicModuleLoader('modules_test_set1', 
						  'modules_test_set2', 
						  'modules_test_set3/module33.py', 
						  'fake/path/pointing/to/nothing', 
						  debug=True)

from module22 import foo as foo22
foo22()

from module33 import foo as foo33
foo33()



#dml.print_info()
#dml.print_full_info()

