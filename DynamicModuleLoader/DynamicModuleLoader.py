# -*- coding: utf-8 -*-
import sys, imp, os.path

class DynamicModuleLoader:
	"""Load modules into syspath from files or directories"""
	_loaded_modules = []
	debug = False
	
	def __init__(self, *args, **kwargs):
		"""Tries to load files and directories especified in *args
		
		Limitations: only import source code modules (.py), ignoring dynamic and compiled modules."""
		
		if kwargs.has_key('debug') and kwargs['debug'] == True:
			self.debug = True
			print " -> DEBUG ENABLED"
			
		for a in args:
			if self.debug: print " -> Procesing path", a
			if os.path.exists(a):
				if os.path.isfile(a):
					self.__load_module_from_file(a)
				elif os.path.isdir(a):
					os.path.walk(a, self.__load_modules_from_dir, None)
			else:
				if self.debug: print " -> The path " + a + " does not exists."
				
	def print_info(self):
		"""Prints some basic info about the loaded modules"""
		
		if len(self._loaded_modules) > 0:
			print "\n".join(self._loaded_modules)
			
	def print_full_info(self):
		"""Prints info about *all* modules currently loaded"""
		
		print "\n".join([str(m) for n,m in sys.modules.items()])
		
	def get_loaded_modules(self):
		return self._loaded_modules
			
	def __load_modules_from_dir(self, arg, dirname, names):
		"""Loads all modules in this directory"""
		
		for n in names:
			path = os.path.join(dirname, n)
			self.__load_module_from_file(path)
		
	def __load_module_from_file(self, path):
		"""Loads a module from a path"""
		
		file_name = os.path.basename(path)
		if file_name[-3:].lower() == '.py':
			try:
				if file_name == '__init__.py':
					module_name = os.path.split(os.path.split(path)[0])[-1]
				else:
					module_name = file_name[:-3]
				imp.load_source(module_name, path)
				if self.debug: print " -> Succesfully imported module " + module_name + " from file " + path
				self._loaded_modules.append(module_name)
			except:
				if self.debug: print " -> Error while importing python code from file " + path
		else:
			if self.debug: print " -> Ignoring file " + path
		