import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["figure.dpi"] = 160

fig, ax = plt.subplots(figsize=(11, 6))
fig.patch.set_facecolor("#0f172a")
ax.set_facecolor("#0f172a")

t = np.arange(0, 31)

# Ejemplos ilustrativos
vanishing = 0.72 ** t
exploding = 1.18 ** t

ax.plot(
    t,
    vanishing,
    linewidth=2.8,
    label="Gradiente desvaneciente"
)

ax.plot(
    t,
    exploding,
    linewidth=2.8,
    label="Gradiente explosivo"
)

ax.set_yscale("log")

ax.set_title(
    "Problemas del gradiente en RNN",
    fontsize=20,
    fontweight="bold",
    color="white",
    pad=18
)

ax.set_xlabel(
    "Pasos temporales hacia atrás",
    fontsize=12,
    color="#cbd5e1"
)

ax.set_ylabel(
    "Magnitud del gradiente",
    fontsize=12,
    color="#cbd5e1"
)

ax.grid(True, alpha=0.13, which="both")

ax.tick_params(colors="#cbd5e1")

for spine in ax.spines.values():
    spine.set_color("#334155")

leg = ax.legend(
    frameon=True,
    facecolor="#111827",
    edgecolor="#475569",
    fontsize=11
)

for text in leg.get_texts():
    text.set_color("white")

ax.text(
    2.5, 0.015,
    "Se hace cada vez más pequeño",
    color="#cbd5e1",
    fontsize=10
)

ax.text(
    18.5, 1.5,
    "Crece rápidamente",
    color="#cbd5e1",
    fontsize=10
)

plt.tight_layout()
plt.show()