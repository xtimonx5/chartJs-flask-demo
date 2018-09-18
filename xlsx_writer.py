import os

import xlsxwriter
import datetime

REPORT_URL = '/reports/{}'
REPORTS_ROOT = 'reports'


class XlsxWriter(object):
    def __init__(self, data_set):
        self.data_set = data_set
        self.filename = 'report_{}.xlsx'.format(str(datetime.datetime.now()))
        self.filepath = os.path.join(REPORTS_ROOT, self.filename)
        self.wb = xlsxwriter.Workbook(self.filepath)

    def generate_report(self):
        worksheet = self.wb.add_worksheet('report')
        worksheet.set_column(0, 3, 15)
        for r, row in enumerate(self.data_set):
            for c, v in enumerate(row):
                try:
                    v = float(v)
                except:
                    pass
                worksheet.write(r, c, v)

        self.insert_chart(worksheet)
        self.wb.close()

    def get_link_for_workbook(self):
        return REPORT_URL.format(self.filename)

    def insert_chart(self, ws):
        chart1 = self.wb.add_chart({'type': 'line'})

        # Configure the first series.
        chart1.add_series({
            'name': '=report!$B$1',
            'categories': '=report!$A$2:$A${}'.format(len(self.data_set)),
            'values': '=report!$B$2:$B${}'.format(len(self.data_set)),
        })

        # Add a chart title and some axis labels.
        chart1.set_title({'name': 'Results of sample analysis of file'})
        chart1.set_x_axis({'name': 'X value'})
        chart1.set_y_axis({'name': 'Y value'})

        # Set an Excel chart style. Colors with white outline and shadow.
        chart1.set_style(10)

        # Insert the chart into the worksheet (with an offset).
        ws.insert_chart('C2', chart1, {'x_offset': 25, 'y_offset': 10})

        self.wb.close()
