import networkx 
import matplotlib.pyplot as plt
import imageio
import random
import os

def create_random_graph(n=10, p=0.5):
    G = networkx.erdos_renyi_graph(n, p)

def draw_graph(G, current_node, pos, step, folder="frames"):
    colors = ['red' if node == current_node else 'lightblue' for node in G.nodes()]
    plt.figure(figsize=(6, 6))
    networkx.draw(G, pos, with_labels=True, node_color=colors, node_size=600)
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = f"{folder}/frame_{step:03d}.png"
    plt.savefig(filename)
    plt.close()
    return filename

def simulate_random_walk_with_visualization(G, steps=50, save_every=1):
    pos = networkx.spring_layout(G, seed=42)
    current = random.choice(list(G.nodes()))
    saved_frames = []

    for step in range(steps):
        if step % save_every == 0:
            frame = draw_graph(G, current, pos, step)
            saved_frames.append(frame)
        neighbors = list(G.neighbors(current))
        if neighbors:
            current = random.choice(neighbors)
    return saved_frames

def create_gif(frames, output="random_walk.gif", duration=0.3):
    images = [imageio.imread(f) for f in frames]
    imageio.mimsave(output, images, duration=duration)

G = create_random_graph(n=10, p=0.5)
frames = simulate_random_walk_with_visualization(G, steps=60, save_every=2)
create_gif(frames, output="random_walk.gif", duration=0.4)
