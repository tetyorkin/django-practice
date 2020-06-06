from django.shortcuts import render
from app import settings


def read_csv():
    lines = []
    with open(settings.INFLATION_RUSSIA, encoding='utf-8') as csv_file:
        column = csv_file.readline().split(';')
        for raw in csv_file:
            cols = [float(x) if x else '' for x in raw.split(';')]
            cols[0] = int(cols[0])
            lines.append(cols)
    return column, lines


def inflation_view(request):
    template_name = 'inflation.html'
    context = {
        'column': read_csv()[0],
        'lines': read_csv()[1],
    }
    return render(request, template_name, context)


if __name__ == '__main__':
    pass
