from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    return "This is async task"