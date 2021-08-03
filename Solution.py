import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
#Write your code here


# Task1

def test_generate_plot_with_style1():
    with plt.style.context("ggplot"):
        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111)
        sepal_len = [5.01, 5.94, 6.59]
        sepal_wd = [3.42, 2.77, 2.97]
        petal_len = [1.46, 4.26, 5.55]
        petal_wd = [0.24, 1.33, 2.03]
        species = ['setosa', 'versicolor', 'viriginica']
        species_index1 = [0.7, 1.7, 2.7]
        species_index2 = [0.9, 1.9, 2.9]
        species_index3 = [1.1, 2.1, 3.1]
        species_index4 = [1.3, 2.3, 3.3]
        ax.bar(species_index1, sepal_len,width=0.2,label='Sepal Length')
        ax.bar(species_index2, sepal_wd,width=0.2,label='Sepal Width')
        ax.bar(species_index3, petal_len,width=0.2,label='Petal Length')
        ax.bar(species_index4, petal_wd,width=0.2,label='Petal Width')
        species=['setosa', 'versicolor', 'viriginica']
        ax.set(title='Mean Measurements of Iris Species',
        xlabel='Species', ylabel='Iris Measurements (cm)',xlim=(0.5, 3.7), ylim=(0,10))
        quarters = [1.1, 2.1, 3.1]
        ax.set_xticks(quarters)
        ax.set_xticklabels(['setosa', 'versicolor', 'viriginica'])
        ax.legend()
        plt.savefig("plotstyle1.png")

        
test_generate_plot_with_style1()

#Task2
def test_generate_plot_with_style2():
    with plt.style.context("seaborn-colorblind"):
        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111)
        sepal_len = [5.01, 5.94, 6.59]
        sepal_wd = [3.42, 2.77, 2.97]
        petal_len = [1.46, 4.26, 5.55]
        petal_wd = [0.24, 1.33, 2.03]
        species = ['setosa', 'versicolor', 'viriginica']
        species_index1 = [0.7, 1.7, 2.7]
        species_index2 = [0.9, 1.9, 2.9]
        species_index3 = [1.1, 2.1, 3.1]
        species_index4 = [1.3, 2.3, 3.3]
        ax.bar(species_index1, sepal_len,width=0.2,label='Sepal Length')
        ax.bar(species_index2, sepal_wd,width=0.2,label='Sepal Width')
        ax.bar(species_index3, petal_len,width=0.2,label='Petal Length')
        ax.bar(species_index4, petal_wd,width=0.2,label='Petal Width')
        
        species=['setosa', 'versicolor', 'viriginica']
        ax.set(title='Mean Measurements of Iris Species',
        xlabel='Species', ylabel='Iris Measurements (cm)',xlim=(0.5, 3.7), ylim=(0,10))
        quarters = [1.1, 2.1, 3.1]
        ax.set_xticks(quarters)
        ax.set_xticklabels(['setosa', 'versicolor', 'viriginica'])
        ax.legend()
        plt.savefig("plotstyle2.png")
        
    
test_generate_plot_with_style2()    
    
# Task3

def test_generate_plot_with_style3():
    with plt.style.context("grayscale"):
        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111)
        sepal_len = [5.01, 5.94, 6.59]
        sepal_wd = [3.42, 2.77, 2.97]
        petal_len = [1.46, 4.26, 5.55]
        petal_wd = [0.24, 1.33, 2.03]
        species = ['setosa', 'versicolor', 'viriginica']
        species_index1 = [0.7, 1.7, 2.7]
        species_index2 = [0.9, 1.9, 2.9]
        species_index3 = [1.1, 2.1, 3.1]
        species_index4 = [1.3, 2.3, 3.3]
        ax.bar(species_index1, sepal_len,width=0.2,label='Sepal Length')
        ax.bar(species_index2, sepal_wd,width=0.2,label='Sepal Width')
        ax.bar(species_index3, petal_len,width=0.2,label='Petal Length')
        ax.bar(species_index4, petal_wd,width=0.2,label='Petal Width')
        
        species=['setosa', 'versicolor', 'viriginica']
        ax.set(title='Mean Measurements of Iris Species',
        xlabel='Species', ylabel='Iris Measurements (cm)',xlim=(0.5, 3.7), ylim=(0,10))
        quarters = [1.1, 2.1, 3.1]
        ax.set_xticks(quarters)
        ax.set_xticklabels(['setosa', 'versicolor', 'viriginica'])
        ax.legend()
        plt.savefig("plotstyle3.png")
        
    
    
    
test_generate_plot_with_style3()
