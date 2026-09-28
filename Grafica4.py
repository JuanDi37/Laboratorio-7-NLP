import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["figure.dpi"] = 160

fig, ax = plt.subplots(figsize=(13, 5.8))
fig.patch.set_facecolor("#0f172a")
ax.set_facecolor("#0f172a")
ax.set_xlim(0, 13)
ax.set_ylim(0, 7)
ax.axis("off")

# Colores
text_main = "#f8fafc"
text_sub = "#cbd5e1"
input_edge = "#22d3ee"
hidden_edge = "#a78bfa"
output_edge = "#f472b6"
node_fill = "#111827"

# Posiciones
xs = [2, 6, 10]
input_y = 1.5
hidden_y = 4
output_y = 6

words = ["el", "gato", "duerme"]

def draw_node(x, y, label, edgecolor, radius=0.42):
    ax.add_patch(
        Circle((x, y), radius * 1.08,
               color=edgecolor, alpha=0.10, lw=0)
    )
    ax.add_patch(
        Circle((x, y), radius,
               facecolor=node_fill,
               edgecolor=edgecolor,
               linewidth=2.3,
               zorder=3)
    )
    ax.text(
        x, y, label,
        ha="center", va="center",
        color=text_main,
        fontsize=12,
        fontweight="bold",
        zorder=4
    )

def draw_arrow(x1, y1, x2, y2, color, width=1.9):
    ax.add_patch(
        FancyArrowPatch(
            (x1, y1), (x2, y2),
            arrowstyle="->",
            mutation_scale=13,
            linewidth=width,
            color=color,
            alpha=0.75
        )
    )

# Título
ax.text(
    6.5, 6.72,
    'RNN desenrollada en el tiempo: "el gato duerme"',
    ha="center",
    va="center",
    color=text_main,
    fontsize=18,
    fontweight="bold"
)

ax.plot([1, 12], [6.45, 6.45],
        color="#334155", linewidth=1)

# Nodos
for i in range(3):
    draw_node(xs[i], input_y, f"x{i+1}", input_edge)
    draw_node(xs[i], hidden_y, f"h{i+1}", hidden_edge)
    draw_node(xs[i], output_y, f"y{i+1}", output_edge)

# Entrada -> estado oculto
for x in xs:
    draw_arrow(x, input_y + 0.42,
               x, hidden_y - 0.42,
               input_edge)

# Estado oculto -> salida
for x in xs:
    draw_arrow(x, hidden_y + 0.42,
               x, output_y - 0.42,
               output_edge)

# Estado oculto -> siguiente estado
for i in range(2):
    draw_arrow(
        xs[i] + 0.42, hidden_y,
        xs[i+1] - 0.42, hidden_y,
        hidden_edge, 2.1
    )

# Etiquetas
ax.text(
    0.7, input_y, "Entrada",
    rotation=90,
    ha="center",
    va="center",
    color=input_edge,
    fontsize=11,
    fontweight="bold"
)

ax.text(
    0.7, hidden_y, "Estado oculto",
    rotation=90,
    ha="center",
    va="center",
    color=hidden_edge,
    fontsize=11,
    fontweight="bold"
)

ax.text(
    0.7, output_y, "Salida",
    rotation=90,
    ha="center",
    va="center",
    color=output_edge,
    fontsize=11,
    fontweight="bold"
)

# Palabras y tiempos
for i, word in enumerate(words):
    ax.text(
        xs[i], 0.70, word,
        ha="center",
        color=text_main,
        fontsize=13,
        fontweight="bold"
    )

    ax.text(
        xs[i], 0.35, f"t = {i+1}",
        ha="center",
        color="#64748b",
        fontsize=9.5
    )



plt.tight_layout()
plt.show()