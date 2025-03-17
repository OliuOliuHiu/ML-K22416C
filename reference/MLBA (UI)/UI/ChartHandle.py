import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
class ChartHandle:
    def visualizeBarPlot(self, figure, canvas, df, columnX, columnY, hueColumn, title):
        figure.clear()
        ax = figure.add_subplot(111)
        ax.ticklabel_format(useOffset=False, style="plain")
        ax.grid()
        ax = sns.barplot(x=columnX, y=columnY, hue=hueColumn, data=df)
        ax.set_xlabel(columnX)
        ax.set_ylabel('Count')
        ax.set_title(title)
        canvas.draw()
    def visualizeStackedBarChart(self, figure, canvas, df, columnX, columnY1, columnY2, title, label1='Yes',
                                 label2='No'):
        figure.clear()
        ax = figure.add_subplot(111)
        ax.ticklabel_format(useOffset=False, style="plain")
        ax.grid()
        bar_width = 0.35
        index = np.arange(len(df[columnX].unique()))
        ax.bar(index, df[columnY1], bar_width, label=label1, zorder=3)
        ax.bar(index, df[columnY2], bar_width, bottom=df[columnY1], label=label2, zorder=3)
        ax.set_xlabel(columnX)
        ax.set_ylabel('Percentage (%)')
        ax.set_title(title)
        ax.set_xticks(index)
        ax.set_xticklabels(df[columnX].unique())
        ax.legend()
        for i, value in enumerate(df[columnY1]):
            ax.text(i, value / 2, f'{value:.1f}%', ha='center', va='center', color='white', zorder=10)

        for i, value in enumerate(df[columnY2]):
            ax.text(i, value + df[columnY1].iloc[i] / 2, f'{value:.1f}%', ha='center', va='center', color='white',
                    zorder=5)
        canvas.draw()
    def visualizeBarComparison(self, figure, canvas, data, ylabel, title1, title2):
        figure.clear()
        axes = figure.subplots(nrows=1, ncols=2, sharey=True)
        for ax in axes:
            ax.grid()
            ax.tick_params(axis='both', which='both', direction='out', length=6, width=2, colors='black',
                           grid_color='gray', grid_alpha=0.5)
        sns.countplot(y=ylabel, data=data[data['TARGET'] == 1],
                      ax=axes[0], palette='coolwarm', legend=False)
        axes[0].set_title(title1, fontsize=8)
        axes[0].set_xlabel('Count')
        axes[0].set_ylabel(ylabel, fontsize=8)
        axes[0].tick_params(axis='y', labelrotation=45)

        sns.countplot(y=ylabel, data=data[data['TARGET'] == 0],
                      ax=axes[1], palette='coolwarm', legend=False)
        axes[1].set_title(title2, fontsize=8)
        axes[1].set_xlabel('Count')
        axes[1].set_ylabel('')

        plt.tight_layout()
        canvas.draw()

