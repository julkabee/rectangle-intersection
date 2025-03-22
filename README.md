# Rectangle Intersection API

FastAPI-сервис для вычисления пересечения прямоугольников A `(0, 0, 1000, 500)` и произвольного прямоугольника B. Проект разработан как тестовое задание и предоставляет REST API для расчета параметров пересечения двух прямоугольников.

## Описание проекта
Сервис принимает параметры прямоугольника B в формате `(x, y, w, h)` (координаты левого нижнего угла, ширина и высота) и возвращает параметры пересечения с фиксированным прямоугольником A `(0, 0, 1000, 500)` в виде `(x, y, w, h)` или `null`, если пересечения нет. Реализован с использованием FastAPI.

## Требования
- Python 3.9+
- Docker (для запуска в контейнере)
- Git (для клонирования репозитория)

## Установка и запуск локально
1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/your-username/rectangle-intersection.git
   cd rectangle-intersection
    ```
2. **Создайте виртуальное окружение (рекомендуется)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для macOS/Linux
   venv\Scripts\activate     # Для Windows
    ```
3. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
    ```
4. **Запустите сервис локально**:
   ```bash
   uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
    ```
   - Флаг --reload включает автоматическую перезагрузку при изменении кода (удобно для разработки).
5. **Проверьте доступность**:
   - Документация: http://127.0.0.1:8000/docs

## Запуск через Docker
1. **Соберите образ**:
   ```bash
   docker build -t rectangle-intersection .
    ```
2. **Запустите контейнер**:
   ```bash
   docker run -p 8000:8000 rectangle-intersection
    ```
3. **Проверьте доступность**:
   - Документация: http://127.0.0.1:8000/docs

## Экспорт Docker-образа
**Сохраните образ в файл .tar**:
   ```bash
   docker save -o rectangle-intersection.tar rectangle-intersection
   ```

## Запуск через Docker
1. **Загрузите образ в Docker**:
   ```bash
   docker load -i rectangle-intersection.tar
    ```
2. **Запустите контейнер**:
   ```bash
   docker run -p 8000:8000 rectangle-intersection
    ```
3. **Проверьте доступность**:
   - Документация: http://127.0.0.1:8000/docs

## Тестирование
**Проект включает тесты с покрытием кода. Для запуска:**
1. **Убедитесь, что зависимости установлены**:
   ```bash
   pip install -r requirements.txt
    ```
2. **Выполните тесты**:
   ```bash
   pytest tests/ --cov=src/ --cov-report=html
    ```
3. **Отчет о покрытии доступен в** *htmlcov/index.html*:
