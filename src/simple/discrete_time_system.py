from pydrake.systems.framework import VectorSystem

# Define the system.
class SimpleDiscreteTimeSystem(VectorSystem):
    def __init__(self):
        VectorSystem.__init__(self,
            0,                                    # Zero inputs.
            1)                                    # One output.
        self.DeclareDiscreteState(1)             # One state variable.
        self.DeclarePeriodicDiscreteUpdate(1.0)  # One second timestep.

    # x[n+1] = x[n]^3
    def DoCalcVectorDiscreteVariableUpdates(self, context, u, x, xnext):
        xnext[:] = x**3

    # y[n] = x[n]
    def DoCalcVectorOutput(self, context, u, x, y):
        y[:] = x