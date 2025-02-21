import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

arial_path = os.path.join(os.environ['WINDIR'], 'Fonts', 'arial.ttf')


pdfmetrics.registerFont(TTFont('Arial', arial_path))

def generate_pdf(filename):
    document = SimpleDocTemplate(filename, pagesize=letter)
    content = []

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='CustomTitle', fontName='Arial', fontSize=16, alignment=1))
    styles.add(ParagraphStyle(name='CustomBody', fontName='Arial', fontSize=12))

    title = Paragraph("<b>Отчет по заказам ГБПОУИО ИАТ</b>", styles['CustomTitle'])
    content.append(title)

    content.append(Spacer(1, 20))

    data = [
        ['№', 'Заказчик', 'Исполнитель', 'Сумма'],
        [1, 'Касьяненко С.Н.', 'Русинов А.А.', '150000'],
        [2, 'Чернигов П.Н.', 'Минаева М.Д.', '200000'],
        [3, 'Волков В.Б.', 'Данилов Н.А', '300000'],
    ]

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    content.append(table)

    document.build(content)

generate_pdf("adjutanted.pdf")