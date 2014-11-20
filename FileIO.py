import pysal

def openFile(connectionString, mode='r'):
    shp = pysal.pysal.core.FileIO.FileIO.open(connectionString, mode='r')  # @UndefinedVariable
    shp.seek(0)
