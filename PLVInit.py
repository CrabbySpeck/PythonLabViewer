#Imports Go Here, Primarily for the main PythonLabViewer File.
import platform
#import PythonLabViewer as plv

def Main():
    print("Python Lab Viewer Initialization Program\n")
    print("CRAB8012\nGreen_Cafe\n\nYou are running PythonLabViewer on: ")
    OperatingSystem = platform.system()
    print(OperatingSystem)
    #plv.Main(OperatingSystem)
    
    
Main()
