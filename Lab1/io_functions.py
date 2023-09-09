import pandas as pd
pd.set_option('display.max_columns', None)


class IOFunctions:
    @staticmethod
    def read_file_to_list(filename):
        values = []
        with open(filename, 'r') as f:
            for line in f:
                split_line_values = line.split(",")
                values.append(split_line_values)
        return values

    @staticmethod
    def read_file_to_dictionary(filename):
        values = {}
        with open(filename, 'r') as f:
            for no, line in enumerate(f):
                if no == 0:
                    split_line_values = line.split(",")
                    for key in split_line_values:
                        values[key.strip()] = []
                else:
                    split_line_values = line.split(",")
                    for j, key in enumerate(values.keys()):
                        split_line_values = line.split(",")
                        current_string = split_line_values[j].strip()
                        result = IOFunctions.test_if_float(current_string)
                        if result:
                            current_string = float(current_string)
                        values[key].append(current_string)
        return values

    @staticmethod
    def read_file_to_dataframe(filename):
        file_as_dictionary = IOFunctions.read_file_to_dictionary(filename)
        df = pd.DataFrame(file_as_dictionary)
        return df

    @staticmethod
    def test_if_float(input_string):
        try:
            result = float(input_string)
            return True
        except (TypeError, ValueError):
            return False


