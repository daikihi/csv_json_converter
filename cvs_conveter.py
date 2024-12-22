
def load_from_file(file_name: str):
    print(file_name)
    f = open(file_name, 'r')
    data = f.read()
    print(data)
    f.close
    return data

def prepare_from_args():
    import sys

    _file_name = sys.argv
    del _file_name[0]
    print(_file_name)
    return _file_name

def convert_array_line_by_line(data):
    print("data  = " + data)
    lines: list[str] = data.splitlines()
    print(lines)
    return lines

def convert_model_from_lines(lines: list[str]):
    beekeepers = []
    for line in lines:
        ele: list[str] = line.split(",")
        size = len(ele)
        if(size == 5):
            id = ele[0]
            name = ele[1]
            product = ele[2]
            prefecture = ele[3]
            link = ele[4]
            bk = Beekeeper(id, name, product, prefecture, link)
            beekeepers.append(bk)
        else:
            print("ERROR!!! size = " + str(size) + " -- " + line)

# Beekeeper : this is a model class of beekeeper 
# CSV file should be same format with this class
class Beekeeper:
    def __init__(self, id, name,product_name,  prefecture, link):
        self.id = id
        self.name = name
        self.product_name = product_name
        self.prefecture = prefecture
        self.link = link
    
    def print(self):
        print("name = " + self.name + ", prefecture = " + self.prefecture)


_file_name = prepare_from_args()
_file_data = load_from_file(file_name = _file_name[0])
_lines = convert_array_line_by_line(_file_data)
convert_model_from_lines(_lines)

