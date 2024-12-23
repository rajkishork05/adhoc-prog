import matplotlib.pyplot as plt
import random

def simulate_tcp():
    sw_size, total_pkts, loss_prob = 2, 10, 0.1
    sent, acked, timeline = 0, 0, ["SYN ->", "<- SYN-ACK", "ACK ->"]
    print("Connection Established!\nStarting Data Transfer...")
    
    while acked < total_pkts:
        for _ in range(min(sw_size, total_pkts - sent)):
            sent += 1
            timeline.append(f"Packet {sent} ->")
            print(f"Sent: Packet {sent}")
        
        for _ in range(min(sw_size, sent - acked)):
            if random.random() < loss_prob:
                timeline.append(f"<- Packet {acked + 1} LOST")
                print(f"Packet {acked + 1} LOST")
            else:
                acked += 1
                timeline.append(f"<- ACK {acked}")
                print(f"Received: ACK {acked}")
    
    timeline.append("Data Transfer Complete")
    print("\nData Transfer Complete!")
    return timeline

def visualize_timeline(timeline):
    plt.figure(figsize=(8, len(timeline) * 0.4))
    y_positions = range(len(timeline))  # Create compact vertical positions
    
    for y, event in zip(y_positions, timeline):
        plt.text(0.5, len(timeline) - y, event, fontsize=10, ha='center', 
                 bbox=dict(facecolor='lightblue', edgecolor='black'))
    
    plt.axis('off')  # Turn off the axes
    plt.title("TCP Event Timeline", fontsize=14)
    plt.tight_layout()
    plt.show()

# Run the simulation and visualize the timeline
visualize_timeline(simulate_tcp())
