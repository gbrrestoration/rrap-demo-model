
class demo_model():
    """ 
    Demo
    """

    @staticmethod
    def ID():
        return 'demo'

    def __init__(self):
        '''Load all required input data and parameters'''
        return None

    def reset(self):
        '''Reset model parameters'''

    def runtimestep(self):
        '''Usually this is where science happens, however this is just a demo'''
        with open('readme.txt', 'w') as f:
            f.write('demo results')
