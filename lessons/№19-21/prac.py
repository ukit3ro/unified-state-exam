import concurrent.futures

def compute(n):
    n2 = bin(n)[2:]
    n2 += '0' + bin(n % 3)[2:]
    n2 += '0' + bin(int(n2, 2) % 5)[2:]
    R = int(n2, 2)
    return 1  # Возвращаем 1 для увеличения счетчика

def main():
    cnt = 0
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Создаем генератор с задачами для выполнения в пуле процессов
        tasks = (executor.submit(compute, n) for n in range(1, 1000000000))
        # Используем as_completed для получения результатов по мере их выполнения
        for future in concurrent.futures.as_completed(tasks):
            cnt += future.result()  # Увеличиваем счетчик на результат выполнения задачи
    print(cnt)

if __name__ == "__main__":
    main()
