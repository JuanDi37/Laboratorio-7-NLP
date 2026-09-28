import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["figure.dpi"] = 160

fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor("#0f172a")
ax.set_facecolor("#0f172a")
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis("off")

# Nodos
inputs = [(1.2, 5.9), (1.2, 4.0), (1.2, 2.1)]
hidden = [(4.8, 6.0), (4.8, 4.7), (4.8, 3.4), (4.8, 2.1)]
outputs = [(8.7, 5.0), (8.7, 2.4)]

# Colores
input_edge = "#22d3ee"
hidden_edge = "#a78bfa"
output_edge = "#f472b6"
input_fill = "#111827"
hidden_fill = "#111827"
output_fill = "#111827"
text_main = "#f8fafc"
line_input_hidden = "#38bdf8"
line_hidden_output = "#fb7185"

def draw_node(x, y, label, edgecolor, facecolor, r=0.33):
    ax.add_patch(Circle((x, y), r, facecolor=facecolor, edgecolor=edgecolor, linewidth=2.2, zorder=3))
    ax.text(x, y, label, ha="center", va="center", color=text_main, fontsize=13, fontweight="bold", zorder=4)

def connect(a, b, color, alpha=0.35):
    for x1, y1 in a:
        for x2, y2 in b:
            ax.add_patch(
                FancyArrowPatch(
                    (x1 + 0.33, y1),
                    (x2 - 0.33, y2),
                    arrowstyle="-",
                    linewidth=1.2,
                    color=color,
                    alpha=alpha,
                    zorder=1,
                )
            )

# Conexiones
connect(inputs, hidden, line_input_hidden, alpha=0.32)
connect(hidden, outputs, line_hidden_output, alpha=0.38)

# Nodos
for i, (x, y) in enumerate(inputs, start=1):
    draw_node(x, y, f"x{i}", input_edge, input_fill)

for i, (x, y) in enumerate(hidden, start=1):
    draw_node(x, y, f"h{i}", hidden_edge, hidden_fill)

for i, (x, y) in enumerate(outputs, start=1):
    draw_node(x, y, f"y{i}", output_edge, output_fill)

# Etiquetas de capas
ax.text(1.2, 6.7, "ENTRADA", ha="center", va="center", color=input_edge, fontsize=12, fontweight="bold")
ax.text(4.8, 6.7, "CAPA OCULTA", ha="center", va="center", color=hidden_edge, fontsize=12, fontweight="bold")
ax.text(8.7, 5.8, "SALIDA", ha="center", va="center", color=output_edge, fontsize=12, fontweight="bold")

# Título
ax.text(
    5.0,
    7.55,
    "Red neuronal pequeña: 3 entradas → 4 neuronas ocultas → 2 salidas",
    ha="center",
    va="center",
    color=text_main,
    fontsize=18,
    fontweight="bold",
)

# Línea decorativa
ax.plot([0.6, 9.4], [7.25, 7.25], color="#334155", linewidth=1)

# Texto corto abajo, sin cuadros
ax.text(
    5.0,
    0.75,
    "Pesos: 3×4 + 4×2 = 20    |    Sesgos: 4 + 2 = 6",
    ha="center",
    va="center",
    color=text_main,
    fontsize=13,
    fontweight="bold",
)

ax.text(
    5.0,
    0.35,
    "Cada neurona de una capa se conecta con todas las de la siguiente.",
    ha="center",
    va="center",
    color="#cbd5e1",
    fontsize=10.5,
)

plt.tight_layout(pad=1.0)
plt.show()