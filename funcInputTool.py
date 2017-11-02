import pygame, math, time
from appJar import gui

def init():
    global frequency
    frequency = 10
    
    global amplitude
    amplitude = 1
    
    global func
    func = math.sin    

    frequency, amplitude, func = getInput()

def getInput(frequency, amplitude, func, debug=False):
    def press(name):
        nonlocal frequency, amplitude, func
        if debug: print(name)
        if name == 'Cancel':
            win.stop()

        elif name == 'Submit':
            entries = win.getAllEntries()
            if entries['Frequency'].isdigit() and entries['Amplitude'].isdigit():
                frequency = int(entries['Frequency'])
                amplitude = int(entries['Amplitude'])
                
                selectedFunc = win.getOptionBox('Functions')
                if selectedFunc == 'sin':
                    func = math.sin
                elif selectedFunc == 'cos':
                    func = math.cos
                elif selectedFunc == 'tan':
                    func = math.tan
                win.stop()
                return frequency, amplitude, func
        elif name == 'Reset':
            win.setEntry('Frequency', '10')
            win.setEntry('Amplitude', '1')
            win.setOptionBox('Functions', 0)

    win = gui('sine.py input')
    win.setGeometry('400x200')
    win.setFont(20)
    
    win.addLabelEntry('Frequency')
    win.setEntry('Frequency', str(frequency))
    
    win.addLabelEntry('Amplitude')
    win.setEntry('Amplitude', str(amplitude))

    win.addLabelOptionBox('Functions', ['sin', 'cos', 'tan'])

    win.addButtons(['Submit', 'Reset', 'Cancel'], press)
    
    win.go()
    return frequency, amplitude, func

def main():
    print(frequency, amplitude, func)
    
if __name__ == '__main__':
    init()
    main()

