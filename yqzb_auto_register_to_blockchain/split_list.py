import json

check_list = []


def list_of_groups(init_list, children_list_len):
    list_of_groups = zip(*(iter(init_list),) *children_list_len)
    end_list = [list(i) for i in list_of_groups]
    count = len(init_list) % children_list_len
    end_list.append(init_list[-count:]) if count !=0 else end_list
    return end_list

if __name__ == '__main__':
    with open("./read.txt") as f:
        file_content = f.read()
        file_content_json = json.loads(file_content)
        result_list = []
        print("读取到的总长度为",len(file_content_json['jgid_list']))
        for bbslbh_item in file_content_json['jgid_list']:
            if bbslbh_item['jgid'] in check_list:
                pass
            else:
                result_list.append(bbslbh_item)
        print("检查后剩余长度为",len(result_list))
        child_result_list = list_of_groups(result_list,50)
        for child_result in child_result_list:
            print(child_result)
