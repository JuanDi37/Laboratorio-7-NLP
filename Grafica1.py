import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["figure.dpi"] = 160

fig, ax = plt.subplots(figsize=(11, 5.5))
fig.patch.set_facecolor("#0f172a")
ax.set_facecolor("#0f172a")
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

# -----------------------------
# Posiciones
# -----------------------------
inputs = [(1.1, 4.5), (1.1, 3.0), (1.1, 1.5)]
perceptron = (5.0, 3.0)
output = (8.9, 3.0)
bias = (5.0, 0.7)

# -----------------------------
# Colores
# -----------------------------
text_main = "#f8fafc"
text_sub = "#cbd5e1"
input_edge = "#22d3ee"
core_edge = "#a78bfa"
output_edge = "#f472b6"
line_input = "#38bdf8"
line_bias = "#fb7185"
node_fill = "#111827"

# -----------------------------
# Fondo suave decorativo
# -----------------------------
ax.add_patch(Circle((2.1, 4.7), 1.4, color="#22d3ee", alpha=0.06, lw=0))
ax.add_patch(Circle((5.2, 3.0), 1.8, color="#a78bfa", alpha=0.07, lw=0))
ax.add_patch(Circle((8.3, 1.8), 1.1, color="#f472b6", alpha=0.06, lw=0))

# Línea superior sutil
ax.plot([0.7, 9.3], [5.35, 5.35], color="#334155", linewidth=1)

# -----------------------------
# Título
# -----------------------------
ax.text(
    5.0,
    5.72,
    "Perceptrón / Neurona artificial",
    ha="center",
    va="center",
    color=text_main,
    fontsize=16,
    fontweight="bold",
)

# -----------------------------
# Función para nodos
# -----------------------------
def draw_node(x, y, label, edgecolor, radius=0.36, fontsize=12):
    ax.add_patch(Circle((x, y), radius * 1.08, color=edgecolor, alpha=0.12, lw=0))
    ax.add_patch(
        Circle(
            (x, y),
            radius,
            facecolor=node_fill,
            edgecolor=edgecolor,
            linewidth=2.3,
            zorder=3,
        )
    )
    ax.text(
        x,
        y,
        label,
        ha="center",
        va="center",
        fontsize=fontsize,
        color=text_main,
        fontweight="bold",
        zorder=4,
    )

# -----------------------------
# Nodos
# -----------------------------
for i, (x, y) in enumerate(inputs, start=1):
    draw_node(x, y, f"x{i}", input_edge)

draw_node(perceptron[0], perceptron[1], "Σ\n+ b", core_edge, radius=0.55, fontsize=11)
draw_node(output[0], output[1], "y", output_edge)
draw_node(bias[0], bias[1], "b", "#94a3b8", radius=0.26, fontsize=11)

# Etiquetas de sección
ax.text(1.1, 5.0, "ENTRADAS", ha="center", color=input_edge, fontsize=11, fontweight="bold")
ax.text(5.0, 4.25, "SUMA + ACTIVACIÓN", ha="center", color=core_edge, fontsize=11, fontweight="bold")
ax.text(8.9, 5.0, "SALIDA", ha="center", color=output_edge, fontsize=11, fontweight="bold")

# -----------------------------
# Flechas
# -----------------------------
for i, (x, y) in enumerate(inputs, start=1):
    ax.add_patch(
        FancyArrowPatch(
            (x + 0.36, y),
            (perceptron[0] - 0.55, perceptron[1] + (y - perceptron[1]) * 0.08),
            arrowstyle="->",
            mutation_scale=14,
            linewidth=1.9,
            color=line_input,
            alpha=0.75,
        )
    )
    ax.text(
        (x + perceptron[0]) / 2 - 0.15,
        y + 0.15,
        f"w{i}",
        fontsize=10.5,
        color=text_sub,
        fontweight="bold",
    )

# Flecha del bias
ax.add_patch(
    FancyArrowPatch(
        (bias[0], bias[1] + 0.26),
        (perceptron[0], perceptron[1] - 0.55),
        arrowstyle="->",
        mutation_scale=14,
        linewidth=1.9,
        color=line_bias,
        alpha=0.8,
    )
)

# Flecha de salida
ax.add_patch(
    FancyArrowPatch(
        (perceptron[0] + 0.55, perceptron[1]),
        (output[0] - 0.36, output[1]),
        arrowstyle="->",
        mutation_scale=14,
        linewidth=2.0,
        color=output_edge,
        alpha=0.85,
    )
)

# -----------------------------
# Nota inferior
# -----------------------------
ax.text(
    5.0,
    0.25,
    r"$y = f(w_1x_1 + w_2x_2 + w_3x_3 + b)$",
    ha="center",
    va="center",
    color=text_sub,
    fontsize=12.5,
)

plt.tight_layout(pad=1.2)
plt.show()