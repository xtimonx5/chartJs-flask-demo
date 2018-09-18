import json
import petl as etl

from xlsx_writer import XlsxWriter


class FileParser(object):
    def __init__(self, file):
        self.file = file
        self.valid = False

    def is_valid(self):
        try:
            self.petl_table = etl.fromtsv(self.file) \
                .pushheader(['x', ]) \
                .addfield('y', lambda v: v['x'].split(' ')[-1]) \
                .convert({'x': lambda v: v.split(' ')[0]})

            print('{} to process'.format(self.petl_table))
        except:
            return False
        self.valid = True
        return True

    def get_petl_table(self):
        if not self.valid:
            raise AssertionError('You should call {}.is_valid() first'.format(self.__class__.__name__))

        return self.petl_table

    def get_points_json(self):
        if not self.valid:
            raise AssertionError('You should call {}.is_valid() first'.format(self.__class__.__name__))

        points_list = [{'x': float(row[0]), 'y': float(row[1])} for row in self.get_petl_table() if
                       row[0] not in ['x', 'y']]
        print(json.dumps(points_list))
        return json.dumps(points_list)

    def get_xlsx_report(self):
        if not self.valid:
            raise AssertionError('You should call {}.is_valid() first'.format(self.__class__.__name__))
        writer = XlsxWriter(self.get_petl_table())
        writer.generate_report()
        return writer.get_link_for_workbook()
