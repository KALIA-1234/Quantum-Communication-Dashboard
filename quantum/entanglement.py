from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


def create_entanglement():

    qc = QuantumCircuit(2, 2)

    # Apply Hadamard Gate
    qc.h(0)

    # Apply CNOT Gate
    qc.cx(0, 1)

    # Measure both qubits
    qc.measure([0, 1], [0, 1])

    return qc


def run_entanglement():

    simulator = AerSimulator()

    qc = create_entanglement()

    result = simulator.run(qc, shots=1024).result()

    counts = result.get_counts()

    return qc, counts


def save_histogram(counts):

    fig = plot_histogram(
        counts,
        title="Quantum Entanglement Measurement"
    )

    fig.savefig(
        "static/entanglement_histogram.png",
        bbox_inches="tight"
    )

    plt.close(fig)


def save_circuit(qc):

    circuit_drawer(
        qc,
        output="mpl",
        filename="static/entanglement_circuit.png"
    )

    plt.close("all")
