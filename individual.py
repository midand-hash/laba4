def calculate_distance(v1, v2, s):
    
    if v1 <= v2:
      raise ValueError("Скорость первого автомобиля должна быть больше скорости второго автомобиля")
    
    # Время в часах
    time_in_hours = 30 / 60  # 30 минут = 0.5 часа

    # Расстояние, которое первый автомобиль проедет за 30 минут
    distance_1 = v1 * time_in_hours

    # Расстояние, которое второй автомобиль проедет за 30 минут
    distance_2 = v2 * time_in_hours

    # Увеличившееся расстояние между автомобилями
    increased_distance = distance_1 - distance_2

    # Общее расстояние между автомобилями
    total_distance = s + increased_distance


    return total_distance


if __name__ == "__main__":
    try:
      v1 = float(input("Введите скорость первого автомобиля (км/ч): "))
      v2 = float(input("Введите скорость второго автомобиля (км/ч): "))
      s = float(input("Введите расстояние, на которое первый автомобиль опередил второй (км): "))

      distance = calculate_distance(v1, v2, s)
      print(f"Расстояние между автомобилями через 30 минут: {distance:.2f} км")

    except ValueError as e:
      print(f"Ошибка: {e}")
