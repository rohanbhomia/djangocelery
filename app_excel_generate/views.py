import pandas as pd
from django.http import HttpResponse
import io

class GenerateExcel():

    rename_columns = None
    color_columns = None

    def generate_excel(self, data):
        df = pd.DataFrame(data)
        if self.rename_columns:
            df = df.rename(columns=self.rename_columns)
        excel_buffer = io.BytesIO()
        excel_writer = pd.ExcelWriter(excel_buffer, engine='xlsxwriter')
        df.to_excel(excel_writer, index=False)
        if self.color_columns:
            workbook = excel_writer.book
            worksheet = excel_writer.sheets['Sheet1']
            for cols in self.color_columns:
                cell_format = workbook.add_format({'bg_color': cols.get('color'),'bold': True})  # Red background color
                worksheet.write(cols.get('index'),cols.get('column'), cell_format)
        excel_writer.close()
        excel_buffer.seek(0)
        response = HttpResponse(excel_buffer.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=my_excel_file.xlsx'
        return response