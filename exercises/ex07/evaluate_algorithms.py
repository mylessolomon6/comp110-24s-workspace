__author__ = "730392828"
import matplotlib.pyplot as plt
from exercises.ex07.runtime_analysis_functions import evaluate_runtime
from exercises.ex07.runtime_analysis_functions import evaluate_memory_usage
START_SIZE: int = 0
END_SIZE: int = 1000


times = evaluate_runtime("selection_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Selection Sort - mylesmyl")
plt.show()


times = evaluate_runtime("insertion_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Insertion Sort - mylesmyl")
plt.show()


usage = evaluate_memory_usage("selection_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Selection Sort - mylesmyl")
plt.show()


usage = evaluate_memory_usage("insertion_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Insertion Sort - mylesmyl")
plt.show()