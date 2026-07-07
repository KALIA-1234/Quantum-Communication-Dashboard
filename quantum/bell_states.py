from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.visualization import circuit_drawer
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


def create_bell():
    qc = QuantumCircuit(2, 2)

    qc.h(0)
    qc.cx(0, 1)

    qc.measure([0, 1], [0, 1])

    return qc



def run_circuit(qc):

    simulator = AerSimulator()

    result = simulator.run(qc, shots=1024).result()

    return result.get_counts()

def save_circuit(qc):
    circuit_drawer(
        qc,
        output="mpl",
        filename="static/bell_circuit.png"
    )    

def save_histogram(counts):

    fig = plot_histogram(counts)

    plt.savefig("static/bell_histogram.png")

    plt.close(fig)



