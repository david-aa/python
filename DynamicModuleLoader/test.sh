#!/bin/sh

python -c "from DynamicModuleLoader import DynamicModuleLoader; dml = DynamicModuleLoader('modules_test_set1', 'modules_test_set2', 'modules_test_set3/module33.py', 'fake/path/pointing/to/nothing', debug=False); dml.print_full_info()" | grep modules_test