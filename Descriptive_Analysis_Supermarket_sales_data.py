{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "private_outputs": true,
      "provenance": [],
      "cell_execution_strategy": "setup",
      "authorship_tag": "ABX9TyMcXnPXvZ2vim22X8weGqCB",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mandelathomas/Descriptive_Analysis_Supermarket_sales_data/blob/main/Descriptive_Analysis_Supermarket_sales_data.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Tm-X6pF7mkQe"
      },
      "outputs": [],
      "source": [
        "\"\"\"\n",
        "Purpose: Analyzing store data using descriptive analysis and statistic\n",
        "Analyst: Mandela Philip Thomas\n",
        "Date: Feb 14, 2025\n",
        "\"\"\"\n",
        "\n",
        "#---- Loading and Exploring Data----|\n",
        "\n",
        "\n",
        "import pandas as pd\n",
        "from sklearn.datasets import make_blobs\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from sklearn.cluster import KMeans\n",
        "from scipy.cluster.hierarchy import dendrogram, linkage\n",
        "\n",
        "#load dataset\n",
        "data_file = pd.read_csv(\"/content/supermarket_sales.csv\")\n",
        "\n",
        "#display the dataset\n",
        "data_file.head(10)\n",
        "\n",
        "#check basic information about the dataset like (data type, rows and columns and more )\n",
        "data_file.info()\n",
        "\n",
        "#check for missing values in the dataset\n",
        "data_file.isnull().sum()\n",
        "\n",
        "#------ statistic summary for numerical columns ---|\n",
        "\n",
        "#mean, median, and mode\n",
        "data_mean = data_file['gross income'].mean()\n",
        "data_median = data_file['gross income'].median()\n",
        "data_mode = data_file['gross income'].mode()\n",
        "\n",
        "#print out the mean, median and mode\n",
        "print(f'Mean (the Average gross Income ): {data_mean.round(2)}')\n",
        "print(f'Median : {data_median}')\n",
        "print(f'Mode (The most appearing gross income): {data_mode.round(2)}')\n",
        "\n",
        "#standard deviation and variance\n",
        "data_std = data_file['gross income'].std()\n",
        "data_var = data_file['gross income'].var()\n",
        "print(f'Standard Deviation: {data_std}')\n",
        "print(f'Variance: {data_var}')\n",
        "\n",
        "\n",
        "#Visualization\n",
        "\n",
        "#histgram\n",
        "plt.hist(data_file['gross income'], bins=10, edgecolor='black')\n",
        "plt.title('Histogram of Gross Income')\n",
        "plt.xlabel('Gross Income')\n",
        "plt.ylabel('Frequency')\n",
        "plt.show()\n",
        "\n",
        "#box plot\n",
        "plt.boxplot(data_file['gross income'])\n",
        "plt.title('Box Plot of Gross Income')\n",
        "plt.ylabel('Gross Income')\n",
        "plt.show()\n",
        "\n",
        "#bar plot for categorical data (letters data)\n",
        "\n",
        "sns.countplot(x='Product line', data=data_file)\n",
        "plt.title('Bar Plot of Product Line')\n",
        "plt.xlabel('Product Line')\n",
        "plt.ylabel('Frequency')\n",
        "plt.show()\n",
        "\n",
        "\n",
        "#----- Grouped Summary Statistics ----|\n",
        "\n",
        "#group by Gender  and calculate the salary mean\n",
        "gender_stat = data_file.groupby('Gender')['gross income'].mean()\n",
        "print(f'Gender Gross Income \\n \\n{gender_stat}')\n",
        "data_file.head(10)\n",
        "\n",
        "#group by Branch, Rating , and customer type\n",
        "data_audit = data_file.groupby(['Branch', 'Rating', 'Customer type'])['gross income'].mean()\n",
        "print(f'Gross income Audits By Branch \\n \\nBranch, Rating, Customer type Gross Income \\n {data_audit}')\n",
        "\n",
        "\n"
      ]
    }
  ]
}