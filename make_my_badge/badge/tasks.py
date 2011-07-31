from celery.decorators import task

print "loaded"

@task()
def add(x, y):
    return x + y
