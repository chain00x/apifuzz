import argparse

parser = argparse.ArgumentParser(description='apifuzz')
parser.add_argument('-o',type=str,required=False,help='输出文件')
parser.add_argument('-p',type=str,required=True,help='输入参数')

parameter=parser.parse_args().p
output_file=parser.parse_args().o

def generate_path(input_str):
    input_params = input_str.split("/")
    path_list = input_params[0].split(",")
    for i in range(1, len(input_params)):
        old_path_list_len = len(path_list)
        for j in range(0, old_path_list_len):
            for k in input_params[i].split(","):
                path_list.append(path_list[j] + "/" + k)
        path_list = path_list[old_path_list_len:]
    return path_list


if __name__ == '__main__':
    for apipath in generate_path(parameter):
        print(apipath)
        if output_file:
            with open(output_file,'a') as object:
                object.write(apipath+'\n')