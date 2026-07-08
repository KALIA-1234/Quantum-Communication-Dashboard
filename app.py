from flask import Flask, render_template

from quantum.bell_states import (
    create_bell,
    run_circuit,
    save_histogram,
    save_circuit
)

from quantum.entanglement import (
    run_entanglement,
    save_histogram as entanglement_save_histogram
)

from quantum.teleportation import (
    run_teleportation,
    save_histogram as teleportation_save_histogram
)

app = Flask(__name__)


# ---------------- Home ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- Bell States ----------------

@app.route("/bell")
def bell():

    qc = create_bell()

    counts = run_circuit(qc)

    save_histogram(counts)

    save_circuit(qc)

    return render_template(
        "bell.html",
        counts=counts
    )


# ---------------- Entanglement ----------------

@app.route("/entanglement")
def entanglement():

    qc, counts = run_entanglement()

    entanglement_save_histogram(counts)

    from quantum.entanglement import save_circuit
    save_circuit(qc)

    return render_template(
        "entanglement.html",
        counts=counts
    )


# ---------------- Teleportation ----------------

from quantum.teleportation import (
    run_teleportation,
    save_histogram as teleportation_save_histogram,
    save_circuit as teleportation_save_circuit
)

@app.route("/teleportation")
def teleportation():

    qc, counts = run_teleportation()

    teleportation_save_histogram(counts)

    teleportation_save_circuit(qc)

    return render_template(
        "teleportation.html",
        counts=counts
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0",port=10000)
