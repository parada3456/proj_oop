class Chapter:
    __chapter_id = 1

    def __init__(self, chapter_number, name, context, date_time, cost):
        self.__chapter_id += 1
        self.__chapter_number = chapter_number
        self.__name = name
        self.__context = context
        self.__publish_date_time = date_time
        self.__viewer_count = 0
        self.__comment_list = []
        self.__cost = cost

    def add_comment(self, comment):
        self.__comment_list.append(comment)

    def add_viewer_count(self):
        self.__viewer_count += 1

    def update_cost(self, new_cost):
        self.__cost = new_cost

    def update_name(self, new_name):
        self.__name = new_name

    def update_context(self, context):
        self.__context = context