from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import date


pdfmetrics.registerFont(TTFont('Arial', r'C:\Windows\Fonts\Arial.ttf'))

def create_tz_pdf(filename, customer_name, customer_position, contractor_name, contractor_position):
    doc = SimpleDocTemplate(filename, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Left', alignment=TA_LEFT, fontName='Arial', fontSize=10, leading=14))
    styles.add(ParagraphStyle(name='LeftBold', alignment=TA_LEFT, fontName='Arial', fontSize=10, leading=14, bold=True))
    styles.add(ParagraphStyle(name='CustomTitle', alignment=TA_LEFT, fontName='Arial', fontSize=14, leading=18, bold=True))
    styles.add(ParagraphStyle(name='Right', alignment=TA_RIGHT, fontName='Arial', fontSize=10, leading=14))

    content = []

    # Заголовок
    content.append(Paragraph("Техническое задание (ТЗ) на разработку модуля генерации PDF-файлов", styles['CustomTitle']))
    content.append(Spacer(1, 12))

    # Содержание
    sections = [
        ("1. Общие сведения", [
            "1.1. Наименование работы: Разработка программного модуля для генерации PDF-документов в рамках проекта \"Управление документацией\".",
            "1.2. Исполнитель: ООО \"Технологии Развития\".",
            "1.3. Основание для выполнения работы: Договор № 123/45-2025 от 01.01.2025, заключенный между ООО \"Технологии Развития\" и АО \"Системы Документооборота\".",
            "1.4. Цель работы: Создание программного модуля для автоматической генерации PDF-документов на основании структурированных данных с возможностью последующего сохранения и отправки."
        ]),
        ("2. Требования к функционалу", [
            "2.1. Назначение модуля: Модуль предназначен для формирования PDF-документов, содержащих текстовые, табличные и графические данные, с применением заданных шаблонов.",
            "2.2. Основные функции:",
            "- Генерация PDF-документов на основании входных данных в формате JSON.",
            "- Поддержка статических и динамических шаблонов для отображения структуры документа.",
            "- Вставка логотипов, изображений, графиков и таблиц.",
            "- Добавление метаданных к документу (автор, дата создания, заголовок).",
            "- Поддержка локализации (многоязычные документы).",
            "2.3. Требования к входным данным:",
            "- Формат данных: JSON.",
            "- Структура входных данных определяется спецификацией (Приложение 1).",
            "- Входные данные включают: заголовок, текстовые блоки, таблицы, ссылки на изображения, параметры форматирования.",
            "2.4. Требования к выходным данным:",
            "- Формат выходного файла: PDF версии 1.7.",
            "- Генерируемый документ должен соответствовать стандарту PDF/A-1b для долгосрочного хранения.",
            "- Поддержка форматов страниц: A4 (пейзаж и портрет).",
            "- Документ должен содержать сноски, нумерацию страниц и оглавление.",
            "2.5. Дополнительные требования:",
            "- Использование библиотеки Apache PDFBox версии 3.0 или другой, согласованной с заказчиком.",
            "- Ограничение размера файла: не более 15 МБ.",
            "- Возможность добавления водяных знаков и QR-кодов."
        ]),
        ("3. Требования к надежности", [
            "3.1. Производительность:",
            "- Генерация документа объемом до 100 страниц должна выполняться не более чем за 3 секунды на сервере с характеристиками: CPU — 4 ядра, 2.4 GHz; RAM — 8 ГБ.",
            "3.2. Стабильность:",
            "- Модуль должен корректно обрабатывать исключения и предоставлять понятные сообщения об ошибках (логирование)."
        ]),
        ("4. Условия эксплуатации", [
            "- Сервер: ОС Linux Ubuntu 22.04.",
            "4.1. Среда выполнения:",
            "- Язык разработки: Python 3.11",
            "4.2. Ограничения:",
            "- Модуль должен быть совместим с существующей системой документооборота \"DocManager\".",
            "- Использование сторонних библиотек допускается только по согласованию с заказчиком."
        ]),
        ("5. Требования к документированию", [
            "5.1. Техническая документация должна включать:",
            "- Руководство пользователя с примерами использования модуля.",
            "- Инструкция по установке и настройке.",
            "- Описание структуры кода.",
            "5.2. Формат предоставления документации:",
            "Файлы в формате PDF, оформленные в соответствии с ГОСТ 2.105–95."
        ]),
        ("6. Порядок контроля и приемки", [
            "6.1. Этапы проверки:",
            "- Тестирование на предоставленных заказчиком данных.",
            "- Визуальная проверка корректности отображения текста, таблиц и изображений в PDF-документах.",
            "- Проверка совместимости с системой документооборота.",
            "6.2. Критерии приемки:",
            "- Соответствие выходных данных требованиям из раздела 2.4.",
            "- Успешная генерация тестового документа объёмом 50 страниц с таблицами и изображениями.",
            "- Отсутствие ошибок и сбоев при обработке входных данных."
        ]),
        ("7. Сроки выполнения", [
            "Разработка: до 01.03.2025.",
            "Тестирование: с 02.03.2025 по 10.03.2025.",
            "Передача заказчику: 11.03.2025."
        ]),
        ("8. Приложения", [
            "Пример структуры входных данных в формате JSON.",
            "Шаблоны PDF-документов.",
            "Список стандартов ГОСТ для оформления документов."
        ])
    ]

    for section, items in sections:
        content.append(Paragraph(section, styles['LeftBold']))
        content.append(Spacer(1, 6))
        for item in items:
            content.append(Paragraph(item, styles['Left']))
            content.append(Spacer(1, 3))
        content.append(Spacer(1, 12))

        # Добавление даты и подписей в конце 8-го пункта
        if section.startswith("8."):
            content.append(Spacer(1, 24))
            today = date.today().strftime("%d.%m.%Y")
            content.append(Paragraph(f"Дата: {today}", styles['Right']))
            content.append(Spacer(1, 12))
            content.append(Paragraph(f"Заказчик: {customer_name}", styles['Right']))
            content.append(Paragraph(f"Должность: {customer_position}", styles['Right']))
            content.append(Paragraph("____________________", styles['Right']))
            content.append(Spacer(1, 12))
            content.append(Paragraph(f"Исполнитель: {contractor_name}", styles['Right']))
            content.append(Paragraph(f"Должность: {contractor_position}", styles['Right']))
            content.append(Paragraph("____________________", styles['Right']))

    doc.build(content)

customer_name = input("Введите имя заказчика: ")
customer_position = input("Введите должность заказчика: ")
contractor_name = input("Введите имя исполнителя: ")
contractor_position = input("Введите должность исполнителя: ")

create_tz_pdf("adjutanted.pdf", customer_name, customer_position, contractor_name, contractor_position)
print("PDF успешно создан: technical_specification.pdf")