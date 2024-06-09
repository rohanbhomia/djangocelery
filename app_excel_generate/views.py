import pandas as pd
from django.http import HttpResponse
import io


def generate_excel(data):
    df = pd.DataFrame(data)
    excel_buffer = io.BytesIO()
    excel_writer = pd.ExcelWriter(excel_buffer, engine='xlsxwriter')
    df.to_excel(excel_writer, index=False)
    excel_writer.close()
    excel_buffer.seek(0)
    response = HttpResponse(excel_buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=my_excel_file.xlsx'
    return response