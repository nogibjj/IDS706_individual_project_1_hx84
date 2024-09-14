import os
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF


def read_dataset(path):
    """Read dataset from path."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(script_dir, path)
    df = pd.read_csv(dataset_path)
    return df


def statistics(df):
    """Print dataset statistics."""
    print(df.describe())


def save_histogram(df, column_name, save_path):
    """Save histogram for a specific column with mean and median marked."""
    plt.figure(figsize=(10, 6))
    plt.hist(df[column_name], bins=20, color="skyblue", edgecolor="black", alpha=0.7)
    mean = df[column_name].mean()
    median = df[column_name].median()
    plt.axvline(mean, color="r", linestyle="--", linewidth=2, label=f"Mean: {mean:.2f}")
    plt.axvline(median, color="g", linestyle="-", linewidth=2, label=f"Median: {median:.2f}")
    plt.title(f"Distribution of {column_name} for NBA Players")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def calculate_statistics(df, column_name):
    """Calculate mean, median, and standard deviation for a specific column."""
    mean = df[column_name].mean()
    median = df[column_name].median()
    std = df[column_name].std()
    return mean, median, std


def add_statistics_to_pdf(pdf, column_name, mean, median, std):
    """Add statistics for a column to the PDF."""
    pdf.cell(200, 10, txt=f"Mean {column_name}: {mean:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Median {column_name}: {median:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Standard Deviation of {column_name}: {std:.2f}", ln=True)


def generate_pdf(df, pdf_path="NBA_2021_Report.pdf"):
    """Generate dataset statistics report and save it to pdf."""
    pdf = FPDF()

    # Add a page for overall statistics
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="NBA 2021 Statistics Report", ln=True, align="C")

    pdf.set_font("Arial", "B", 12)
    pdf.cell(
        200,
        10,
        txt="Descriptive Statistics for Points (PTS), Assists (AST), and Blocks (BLK)",
        ln=True,
        align="L",
    )

    # Calculate and add statistics for PTS, AST, and BLK
    for column_name in ["PTS", "AST", "BLK"]:
        mean, median, std = calculate_statistics(df, column_name)
        add_statistics_to_pdf(pdf, column_name, mean, median, std)

    # Add histograms to the PDF
    pdf.cell(200, 10, txt="Distribution of Points", ln=True)
    pdf.image("pts_histogram.png", x=10, y=70, w=190)

    pdf.add_page()
    pdf.cell(200, 10, txt="Distribution of Assists", ln=True)
    pdf.image("ast_histogram.png", x=10, y=70, w=190)

    pdf.add_page()
    pdf.cell(200, 10, txt="Distribution of Blocks", ln=True)
    pdf.image("blk_histogram.png", x=10, y=70, w=190)

    pdf.output(pdf_path)
    print(f"PDF report generated: {pdf_path}")


def visualization(df):
    """Generate visualizations and save histograms for PTS, AST, and BLK."""
    save_histogram(df, "PTS", "pts_histogram.png")
    save_histogram(df, "AST", "ast_histogram.png")
    save_histogram(df, "BLK", "blk_histogram.png")


def _file_exists_and_not_empty(filepath):
    return os.path.exists(filepath) and os.path.getsize(filepath) > 0
