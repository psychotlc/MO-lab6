
import dual_problem
from simplex import Simplex
import strategic

if __name__ == '__main__':
    print("\tНайдём смешанные стратегии для игрока А. Сформулируем задачу для решения симплекс-методом:")
    dual_p = dual_problem.DualProblem("input_data.json")

    # Находим опорное решение.
    dual_p.reference_solution()
    # Находим оптимальное решение.
    dual_p.optimal_solution()

    #
    print(strategic.StrategyA(dual_p.simplex_table_))

    print("\tНайдём смешанные стратегии для игрока B. Сформулируем задачу для решения симплекс-методом:")
    problem = Simplex("input_data.json")
    print(problem)

    # Находим опорное решение.
    problem.reference_solution()
    # Находим оптимальное решение.
    problem.optimal_solution()

    print(strategic.StrategyB(problem.simplex_table_))
