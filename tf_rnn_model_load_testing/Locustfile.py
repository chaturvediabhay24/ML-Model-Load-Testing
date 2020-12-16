from locust import   TaskSet, task, between
from locust import HttpLocust 

class TestBehaviour(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass
    # def _get_image_part(self, file_path, file_content_type='image/jpeg'):
    #     import os
    #     file_name = os.path.basename(file_path)
    #     file_content = open(file_path, 'rb')
    #     return file_name, file_content, file_content_type

    @task(1)
    def hello_world(self):
        self.client.post("/", {"experience":"That time of year thou mayst in me behold", "test_score":"2"})

class WebsiteTest(HttpLocust ):
    task_set = TestBehaviour
    wait_time = between(0.5, 3.0)