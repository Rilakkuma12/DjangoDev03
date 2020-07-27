from django.db.models import Count

from interfaces.models import Interfaces


def get_count_by_project(datas):
    """
    1.统计项目中接口、用例、配置、套件的数量
    2.对时间进行格式化
    :param datas:
    :return:
    """
    for item in datas:
        create_time_list = item.get('create_time').split('T')
        first_part = create_time_list[0]
        second_part = create_time_list[1].split('.')[0]
        item['create_time'] = first_part + ' ' + second_part

        project_id = item['id']
        interfaces_testcase_obj = Interfaces.objects.values('id').annotate(testcases=Count('testcases')).\
            filter(project_id=project_id)

    return interfaces_testcase_obj



