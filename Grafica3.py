import numpy as np
import matplotlib.pyplot as plt

# Datos
x = np.linspace(-8, 8, 800)
sigmoid = 1 / (1 + np.exp(-x))
tanh = np.tanh(x)
relu = np.maximum(0, x)

# "Softmax" ilustrativa en 1D: solo para mostrar la idea de una curva positiva
softmax_curve = np.exp(x) / np.sum(np.exp(x))

# Estilo
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["figure.dpi"] = 160

fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor("#0f172a")
ax.set_facecolor("#0f172a")

# Curvas
ax.plot(x, sigmoid, linewidth=2.6, label="Sigmoide")
ax.plot(x, tanh, linewidth=2.6, label="tanh")
ax.plot(x, relu, linewidth=2.6, label="ReLU")
ax.plot(x, softmax_curve, linewidth=2.6, label="softmax (ilustrativa)")

# Ejes y grilla
ax.axhline(0, linewidth=1, alpha=0.4)
ax.axvline(0, linewidth=1, alpha=0.4)
ax.grid(True, alpha=0.12)

ax.set_xlim(-8, 8)
ax.set_ylim(-1.2, 8.3)

# Títulos y etiquetas
ax.set_title("Funciones de activación", fontsize=20, fontweight="bold", color="white", pad=18)
ax.set_xlabel("Entrada x", fontsize=12, color="#cbd5e1")
ax.set_ylabel("Salida f(x)", fontsize=12, color="#cbd5e1")

# Ticks y bordes
ax.tick_params(colors="#cbd5e1")
for spine in ax.spines.values():
    spine.set_color("#334155")

# Leyenda
leg = ax.legend(frameon=True, facecolor="#111827", edgecolor="#475569", fontsize=11)
for text in leg.get_texts():
    text.set_color("white")

# Anotaciones
ax.text(-7.6, 7.55, "Rangos de salida", color="white", fontsize=13, fontweight="bold")
ax.text(
    -7.6, 7.0,
    "Sigmoide: (0, 1)\ntanh: (-1, 1)\nReLU: [0, ∞)\nsoftmax: (0, 1), suma 1",
    color="#cbd5e1",
    fontsize=11,
    va="top"
)

ax.text(2.0, 6.9, "Sigmoide y tanh\nsaturan", color="#cbd5e1", fontsize=10)
ax.text(2.7, 5.8, "ReLU crece linealmente\npara x > 0", color="#cbd5e1", fontsize=10)
ax.text(4.1, 2.9, "softmax se usa en\nsalida multiclase", color="#cbd5e1", fontsize=10)

plt.tight_layout()
plt.show()