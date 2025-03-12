'''Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.'''

def printing_models(*args):
    models=list(args)
    print (models)

printing_models ("modello 1", "modello 2","modello 3")
if __name__=="__main__":
    printing_models ("modello 1", "modello 2","modello 3")

