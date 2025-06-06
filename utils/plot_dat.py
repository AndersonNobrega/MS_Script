import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from paths import CONF_PATH

style_path = CONF_PATH / "paper.mplstyle"
sns.set_theme(style="whitegrid", palette="muted", rc={"axes.edgecolor": "black"})
plt.style.use(style_path)

# Constants
INPUT_FILE_PATH = (
    "/home/anderson/temp/individual_appliances/residencial/train_ar_condicionado.dat"
)
MAX_Y_LIMIT_BUFFER = 200

pt = 1.0 / 72.27
golden = (1 + 5**0.5) / 2
fig_width = 441.0 * pt
PLOT_FIGSIZE = (fig_width, fig_width / golden)


# Load data from pickle file
def load_data(file_path):
    with open(file_path, "rb") as file:
        data = pickle.load(file)
    return data


# Plotting the data
def plot_data(arr):
    max_value = arr[:, 1, 0].max()

    plt.figure(figsize=PLOT_FIGSIZE)

    plt.subplot(211)
    plt.ylabel("Consumo - Potência Ativa (W)")
    plt.plot(arr[:, 1, 0])

    plt.subplot(212)
    plt.subplots_adjust(bottom=0.2)
    plt.xticks(rotation=25)
    plt.title("Consumo Total")
    plt.ylabel("Consumo - Potência Reativa (W)")
    plt.ylim(0, max_value + MAX_Y_LIMIT_BUFFER)
    plt.plot(arr[:, 1, 1])

    plt.show()


def main():
    arr = load_data(INPUT_FILE_PATH)
    print(f"Data Shape: {arr.shape}")
    plot_data(arr)


if __name__ == "__main__":
    main()
