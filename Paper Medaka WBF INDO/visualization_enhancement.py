import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Rectangle
import pandas as pd

# Set style for professional academic plots
plt.style.use("seaborn-v0_8-whitegrid")
sns.set_palette("husl")


# Create enhanced performance comparison chart
def create_performance_radar_chart():
    """Create a comprehensive radar chart comparing ensemble methods"""

    # Performance metrics data
    metrics = [
        "mAP@0.5:0.95",
        "mAP@0.5",
        "Precision",
        "Recall",
        "F1-Score",
        "Stability",
    ]

    # Normalized performance values (0-1 scale)
    single_yolov8 = [
        0.460 / 0.591,
        0.747 / 0.898,
        0.612 / 0.941,
        0.751 / 0.986,
        0.592 / 0.841,
        0.111 / 0.056,
    ]
    nms_ensemble = [
        0.526 / 0.591,
        0.837 / 0.898,
        0.552 / 0.941,
        0.898 / 0.986,
        0.655 / 0.841,
        0.065 / 0.056,
    ]
    wbf_ensemble = [
        0.557 / 0.591,
        0.863 / 0.898,
        0.709 / 0.941,
        0.841 / 0.986,
        0.731 / 0.841,
        0.056 / 0.056,
    ]

    # Number of variables
    N = len(metrics)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    # Initialize the plot
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection="polar"))

    # Add the values for each method
    single_yolov8 += single_yolov8[:1]
    nms_ensemble += nms_ensemble[:1]
    wbf_ensemble += wbf_ensemble[:1]

    # Plot the data
    ax.plot(
        angles, single_yolov8, "o-", linewidth=2, label="Single YOLOv8", color="#FF6B6B"
    )
    ax.fill(angles, single_yolov8, alpha=0.25, color="#FF6B6B")

    ax.plot(
        angles, nms_ensemble, "o-", linewidth=2, label="NMS Ensemble", color="#4ECDC4"
    )
    ax.fill(angles, nms_ensemble, alpha=0.25, color="#4ECDC4")

    ax.plot(
        angles, wbf_ensemble, "o-", linewidth=2, label="WBF Ensemble", color="#45B7D1"
    )
    ax.fill(angles, wbf_ensemble, alpha=0.25, color="#45B7D1")

    # Add labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(metrics)
    ax.set_ylim(0, 1)

    # Add title and legend
    plt.title(
        "Comprehensive Performance Comparison\nAcross Multiple Evaluation Metrics",
        size=16,
        fontweight="bold",
        pad=20,
    )
    plt.legend(loc="upper right", bbox_to_anchor=(1.2, 1.0))

    plt.tight_layout()
    plt.savefig("Images/enhanced_performance_radar.png", dpi=300, bbox_inches="tight")
    plt.close()


def create_confidence_threshold_analysis():
    """Create detailed confidence threshold analysis chart"""

    # Data for confidence threshold analysis
    thresholds = [0.001, 0.25, 0.5, 0.6]

    # mAP values for each method
    single_map = [0.4979, 0.4729, 0.4380, 0.4313]
    nms_map = [0.5351, 0.5300, 0.5210, 0.5185]
    wbf_map = [0.5905, 0.5460, 0.4740, 0.4181]

    # F1-scores for each method
    single_f1 = [0.1472, 0.7617, 0.7648, 0.7726]
    nms_f1 = [0.0265, 0.6121, 0.7344, 0.7345]
    wbf_f1 = [0.0675, 0.8412, 0.8115, 0.7569]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # mAP comparison
    ax1.plot(
        thresholds,
        single_map,
        "o-",
        linewidth=2,
        label="Single YOLOv8",
        color="#FF6B6B",
        markersize=8,
    )
    ax1.plot(
        thresholds,
        nms_map,
        "o-",
        linewidth=2,
        label="NMS Ensemble",
        color="#4ECDC4",
        markersize=8,
    )
    ax1.plot(
        thresholds,
        wbf_map,
        "o-",
        linewidth=2,
        label="WBF Ensemble",
        color="#45B7D1",
        markersize=8,
    )

    ax1.set_xlabel("Confidence Threshold", fontweight="bold")
    ax1.set_ylabel("mAP@0.5:0.95", fontweight="bold")
    ax1.set_title("mAP Performance Across Confidence Thresholds", fontweight="bold")
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_ylim(0.3, 0.65)

    # F1-score comparison
    ax2.plot(
        thresholds,
        single_f1,
        "o-",
        linewidth=2,
        label="Single YOLOv8",
        color="#FF6B6B",
        markersize=8,
    )
    ax2.plot(
        thresholds,
        nms_f1,
        "o-",
        linewidth=2,
        label="NMS Ensemble",
        color="#4ECDC4",
        markersize=8,
    )
    ax2.plot(
        thresholds,
        wbf_f1,
        "o-",
        linewidth=2,
        label="WBF Ensemble",
        color="#45B7D1",
        markersize=8,
    )

    ax2.set_xlabel("Confidence Threshold", fontweight="bold")
    ax2.set_ylabel("F1-Score", fontweight="bold")
    ax2.set_title(
        "F1-Score Performance Across Confidence Thresholds", fontweight="bold"
    )
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_ylim(0, 0.9)

    plt.tight_layout()
    plt.savefig(
        "Images/confidence_threshold_analysis.png", dpi=300, bbox_inches="tight"
    )
    plt.close()


def create_computational_efficiency_chart():
    """Create computational efficiency comparison"""

    methods = ["Single YOLOv8", "NMS Ensemble", "WBF Ensemble"]
    processing_time = [0.221, 0.847, 0.954]
    memory_usage = [2.34, 8.92, 9.87]
    throughput = [16560, 4356, 3780]

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

    # Processing time
    bars1 = ax1.bar(
        methods, processing_time, color=["#FF6B6B", "#4ECDC4", "#45B7D1"], alpha=0.8
    )
    ax1.set_ylabel("Processing Time (seconds)", fontweight="bold")
    ax1.set_title("Average Processing Time per Image", fontweight="bold")
    ax1.set_ylim(0, 1.2)

    # Add value labels on bars
    for bar, value in zip(bars1, processing_time):
        ax1.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.02,
            f"{value:.3f}s",
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    # Memory usage
    bars2 = ax2.bar(
        methods, memory_usage, color=["#FF6B6B", "#4ECDC4", "#45B7D1"], alpha=0.8
    )
    ax2.set_ylabel("Memory Usage (GB)", fontweight="bold")
    ax2.set_title("Peak Memory Consumption", fontweight="bold")
    ax2.set_ylim(0, 12)

    for bar, value in zip(bars2, memory_usage):
        ax2.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.2,
            f"{value:.2f}GB",
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    # Throughput
    bars3 = ax3.bar(
        methods, throughput, color=["#FF6B6B", "#4ECDC4", "#45B7D1"], alpha=0.8
    )
    ax3.set_ylabel("Throughput (images/hour)", fontweight="bold")
    ax3.set_title("Processing Throughput", fontweight="bold")
    ax3.set_ylim(0, 18000)

    for bar, value in zip(bars3, throughput):
        ax3.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 300,
            f"{value:,}",
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    plt.tight_layout()
    plt.savefig(
        "Images/computational_efficiency_comparison.png", dpi=300, bbox_inches="tight"
    )
    plt.close()


def create_species_performance_heatmap():
    """Create species-specific performance heatmap"""

    # Performance data for different species and confidence thresholds
    data = {
        "Method": ["Single YOLOv8", "NMS Ensemble", "WBF Ensemble"] * 2,
        "Species": ["O. celebensis"] * 3 + ["O. javanicus"] * 3,
        "Conf_0.25_P": [0.874, 0.669, 0.950, 0.560, 0.318, 0.673],
        "Conf_0.25_R": [0.813, 0.914, 0.891, 0.843, 0.921, 0.832],
        "Conf_0.25_F1": [0.842, 0.772, 0.919, 0.673, 0.473, 0.744],
        "Conf_0.5_P": [0.914, 0.793, 0.980, 0.660, 0.476, 0.881],
        "Conf_0.5_R": [0.742, 0.898, 0.750, 0.742, 0.888, 0.663],
        "Conf_0.5_F1": [0.819, 0.843, 0.850, 0.698, 0.620, 0.756],
    }

    df = pd.DataFrame(data)

    # Create separate heatmaps for each metric
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle(
        "Species-Specific Performance Analysis Across Confidence Thresholds",
        fontsize=16,
        fontweight="bold",
    )

    metrics = ["P", "R", "F1"]
    conf_levels = ["0.25", "0.5"]

    for i, conf in enumerate(conf_levels):
        for j, metric in enumerate(metrics):
            col_name = f"Conf_{conf}_{metric}"

            # Pivot data for heatmap
            heatmap_data = df.pivot(index="Species", columns="Method", values=col_name)

            # Create heatmap
            sns.heatmap(
                heatmap_data,
                annot=True,
                fmt=".3f",
                cmap="RdYlBu_r",
                ax=axes[i, j],
                cbar_kws={"label": "Score"},
            )

            axes[i, j].set_title(f"Confidence {conf} - {metric}", fontweight="bold")
            axes[i, j].set_xlabel("")
            axes[i, j].set_ylabel("")

    plt.tight_layout()
    plt.savefig("Images/species_performance_heatmap.png", dpi=300, bbox_inches="tight")
    plt.close()


# Generate all visualizations
if __name__ == "__main__":
    print("Generating enhanced visualizations for the paper...")

    create_performance_radar_chart()
    print("✓ Performance radar chart created")

    create_confidence_threshold_analysis()
    print("✓ Confidence threshold analysis created")

    create_computational_efficiency_chart()
    print("✓ Computational efficiency chart created")

    create_species_performance_heatmap()
    print("✓ Species performance heatmap created")

    print("\nAll visualizations have been generated and saved to the Images folder!")
    print("Files created:")
    print("- enhanced_performance_radar.png")
    print("- confidence_threshold_analysis.png")
    print("- computational_efficiency_comparison.png")
    print("- species_performance_heatmap.png")
