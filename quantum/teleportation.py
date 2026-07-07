from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


def create_teleportation():

    qc = QuantumCircuit(3, 3)

    # Create Bell Pair
    qc.h(1)
    qc.cx(1, 2)

    # Prepare state to teleport
    qc.h(0)

    # Bell Measurement
    qc.cx(0, 1)
    qc.h(0)

    # Measure first two qubits
    qc.measure([0, 1], [0, 1])

    # Apply correction operations
    qc.cx(1, 2)
    qc.cz(0, 2)

    # Measure destination qubit
    qc.measure(2, 2)

    return qc


def run_teleportation():

    simulator = AerSimulator()

    qc = create_teleportation()

    result = simulator.run(qc, shots=1024).result()

    counts = result.get_counts()

    return qc, counts


def save_histogram(counts):

    fig = plot_histogram(
        counts,
        title="Quantum Teleportation Measurement"
    )

    fig.savefig(
        "static/teleportation_histogram.png",
        bbox_inches="tight"
    )

    plt.close(fig)


def save_circuit(qc):

    circuit_drawer(
        qc,
        output="mpl",
        filename="static/teleportation_circuit.png"
    )

    plt.close("all")
